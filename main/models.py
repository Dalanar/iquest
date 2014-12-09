from django.db import models


class GiftCardOrder(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)


class QuestOrder(models.Model):
    TIME_CHOICE = (
        (1, "12:00-13:00"),
        (2, "13:00-14:00"),
        (3, "14:00-15:00"),
        (4, "15:00-16:00"),
        (5, "16:00-17:00"),
        (6, "17:00-18:00"),
    )
    QUEST_CHOICE = (
        (1, "Случайный пациент"),
        (2, "Время «Z»"),
    )
    quest = models.CharField(max_length=2, choices=QUEST_CHOICE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=2, choices=TIME_CHOICE)