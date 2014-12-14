from django.db import models


class GiftCardOrder(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Time(models.Model):
    time = models.CharField(max_length=50)
    def __str__(self):
        return self.time


class Quest(models.Model):
    quest = models.CharField(max_length=255)
    def __str__(self):
        return self.quest


class QuestOrder(models.Model):
    quest = models.ForeignKey(Quest)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.ForeignKey(Time)
    # def __str__(self):
    #     return self.QUEST_CHOICE[int(self.quest)][1] + ": " + self.date.isoformat()
