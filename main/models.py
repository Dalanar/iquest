from django.db import models


# Филиал
class Branch(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адрес", null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name="Телефон", null=True, blank=True)
    prefix = models.CharField(max_length=5, verbose_name="Префикс", null=True, blank=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"


# Подарочная карта
class GiftCard(models.Model):
    card_number = models.CharField(max_length=255, verbose_name="Номер карты")
    selling_time = models.DateField(verbose_name="Дата продажи")
    activated_in = models.ForeignKey(Branch, verbose_name="Активирована в", null=True, blank=True)
    activated = models.BooleanField(default=False, verbose_name="Карта активирована")

    def __str__(self):
        return self.card_number

    class Meta:
        verbose_name = "Подарочная карта"
        verbose_name_plural = "Подарочные карты"


# Заявка на карту
class GiftCardOrder(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка на подарочную карту"
        verbose_name_plural = "Заявки на подарочные карты"


# Квесты
class Quest(models.Model):
    quest = models.CharField(max_length=255, verbose_name="Квест")
    alias = models.CharField(max_length=255, verbose_name="Псевдоним для обращения", null=True, blank=True)
    branch = models.ForeignKey(Branch, verbose_name="Филиал", null=True, blank=True)

    def __str__(self):
        return self.quest

    class Meta:
        verbose_name = "Квест"
        verbose_name_plural = "Квесты"


# Баны
class Ban(models.Model):
    ip = models.CharField(max_length=11)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "Бан"
        verbose_name_plural = "Баны"


# Бронирование квеста
class QuestOrder(models.Model):
    """
    Бронирование квеста
    """
    quest = models.ForeignKey(Quest, verbose_name="Квест")
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField()
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    date = models.DateField(verbose_name="Дата")
    time = models.CharField(max_length=10, verbose_name="Время")
    cost = models.IntegerField(max_length=10, verbose_name="Стоимость", primary_key=False, null=True)
    ip = models.CharField(null=True, max_length=11, blank=True)
    notified = models.BooleanField(default=False, verbose_name="Смс уведомление отправлено")

    def __str__(self):
        return self.quest.quest + ": " + self.time + ", " + self.date.isoformat()

    class Meta:
        verbose_name = "Забронированый квест"
        verbose_name_plural = "Забронированные квесты"


# Настройки
class Setting(models.Model):
    """
    Таблица настроек
    """
    key = models.CharField(max_length=255, verbose_name="Ключ")
    value = models.TextField(verbose_name="Значение")

    def __str__(self):
        return self.key + ": " + self.value

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"


# Пустая модель для рассылки в админке
class Delivery(models.Model):
    class Meta(object):
        verbose_name = 'Рассылка'


# Номера телефонов для рассылок
class Phone(models.Model):
    """
    База телефонов для спама
    """
    number = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"


# Смс рассылка
class SmsDelivery(models.Model):
    """
    Смс рассылка
    """
    text = models.TextField(verbose_name="Текст сообщения")
    is_completed = models.BooleanField(default=False, verbose_name="Завершена")

    def __str__(self):
        if self.is_completed:
            text = "Завешено: "
        else:
            text = "Ожидает выполнения: "
        return text + self.text

    class Meta:
        verbose_name = "Смс рассылка"
        verbose_name_plural = "Смс рассылка"


class PhoneDeliveryRelation(models.Model):
    """
    Таблица связи между телефонами и рассылкой
    """
    sms_delivery = models.ForeignKey(SmsDelivery)
    phone = models.ForeignKey(Phone)
