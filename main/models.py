from django.db import models

# class Quest(models.Model):
#     name = models.CharField(max_length=255)
#
# class Booking(models.Model):
#     quest = models.ForeignKey(Quest)


class GiftCardOrder(models.Model):
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


# class QuestOrder(models.Model)