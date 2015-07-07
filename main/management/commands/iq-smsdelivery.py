__author__ = 'Stepan'

from django.core.management.base import BaseCommand
from main.models import SmsDelivery, Phone, PhoneDeliveryRelation
from main.smsc import SMSC


class Command(BaseCommand):
    """
    Сделать рассылку смс сообщений
    """
    help = 'Sms delivery'

    def handle(self, *args, **options):
        try:
            delivery = SmsDelivery.objects.get(is_completed=False)
            completed_phones = \
                PhoneDeliveryRelation\
                    .objects\
                    .filter(sms_delivery=delivery)\
                    .values('phone')
            limit = 50
            phones = \
                Phone.objects.exclude(id__in=completed_phones)[:limit]
            while len(phones):
                self.make_delivery(phones, delivery.text)
                self.add_to_table_relation(delivery, phones)
                phones = \
                    Phone.objects.exclude(id__in=completed_phones)[:limit]
            delivery.is_completed = True
            delivery.save()
            return 0
        except SmsDelivery.DoesNotExist:
            return 0
        except Exception as e:
            print(e)
            return


    def make_delivery(self, phones, text):
        numbers = list(map(lambda phone: phone.number, phones))
        numbers = ";".join(numbers)
        smsc = SMSC()
        smsc.send_sms(numbers, text, sender="iquest")


    def add_to_table_relation(self, delivery, phones):
        for phone in phones:
            relation = PhoneDeliveryRelation(phone=phone, sms_delivery=delivery)
            relation.save()