from django.db import models


class GiftCardOrder(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)


class Quest(models.Model):
    name = models.CharField(max_length=255)


class QuestOrder(models.Model):
    quest = models.ForeignKey(Quest)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()