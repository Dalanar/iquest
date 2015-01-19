from django.db import models


class GiftCardOrder(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подарочная карта"
        verbose_name_plural = "Подарочные карты"


class Quest(models.Model):
    quest = models.CharField(max_length=255, verbose_name="Квест")

    def __str__(self):
        return self.quest

    class Meta:
        verbose_name = "Квест"
        verbose_name_plural = "Квесты"


class QuestOrder(models.Model):
    quest = models.ForeignKey(Quest, verbose_name="Квест")
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField()
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    date = models.DateField(verbose_name="Дата")
    time = models.CharField(max_length=10, verbose_name="Время")
    cost = models.IntegerField(max_length=10, verbose_name="Стоимость", primary_key=False, null=True)

    def __str__(self):
        return self.quest.quest + ": " + self.time + ", " + self.date.isoformat()

    class Meta:
        verbose_name = "Забронированый квест"
        verbose_name_plural = "Забронированные квесты"
