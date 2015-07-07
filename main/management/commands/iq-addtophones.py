__author__ = 'Stepan'

from django.core.management.base import BaseCommand
from main.models import Phone, QuestOrder
from main.utils import *

class Command(BaseCommand):
    """
    Заполняем базу телефонов номерами из броней
    """
    help = 'Add phones to Phone from QuestOrder'

    def handle(self, *args, **options):
        offset = 0
        limit = 100
        orders = QuestOrder.objects.all()[offset:limit]
        while orders:
            for order in orders:
                number = phone_validate(order.phone)
                if number == "":
                    continue
                try:
                    Phone.objects.get(number=number)
                except Phone.DoesNotExist:
                    phone = Phone(number=number)
                    phone.save()
            offset += limit
            orders = QuestOrder.objects.all()[offset:limit]
        return