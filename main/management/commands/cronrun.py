__author__ = 'Stepan'

from django.core.management.base import BaseCommand, CommandError
from main.models import QuestOrder, Setting
from main.smsc import SMSC
from main.utils import *

import datetime, time as ftime


class Command(BaseCommand):
    help = 'Tasks or cron'
    notifyTime = 3600


    def handle(self, *args, **options):
        try:
            now = datetime.datetime.now()
            now_timestamp = int(now.timestamp())
            orders = \
                QuestOrder.objects.filter(
                    date=now.strftime("%Y-%m-%d"), notified=False
                )
            for order in orders:
                order_timestamp = self.__get_order_timestamp(order)
                if order_timestamp - now_timestamp <= self.notifyTime:
                    self.__send_sms(order)
                    self.__notify_order(order)
        except Exception:
            return


    def __notify_order(self, order):
        order.notified = True
        order.save()


    def __send_sms(self, order):
        template = 'Напоминаем, что Вы забронировали игру в IQuest :) "' + \
               order.quest.quest + '" ' + \
               order.date + ' ' +\
               order.time + ' Алтайская 8/3. ' + \
               self.__get_additional_sms_field()
        smsc = SMSC()
        phone = phone_validate(order.phone)
        smsc.send_sms(phone, template, sender="iquest")


    def __get_order_timestamp(self, order):
        date = order.date.strftime("%Y-%m-%d")
        date = date + " " + order.time
        timestamp = \
            int(ftime.mktime(
                datetime.datetime.strptime(date, "%Y-%m-%d %H:%M").timetuple()
            ))
        return timestamp


    def __get_additional_sms_field(self):
        try:
            setting = Setting.objects.get(key="sms-additional")
        except Setting.DoesNotExist:
            return ""
        else:
            return setting.value