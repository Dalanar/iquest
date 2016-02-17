from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ManyToManyField(Branch)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


# Подарочная карта
class GiftCard(models.Model):
    STATUS_CHOICES = (
        ('1', 'В печати'),
        ('2', 'В точке продажи'),
        ('3', 'Продана'),
        ('4', 'Активирована'),
    )

    card_number = models.CharField(max_length=255, verbose_name="Номер карты",
                                   null=True, blank=True)
    selling_time = models.DateField(verbose_name="Дата продажи")
    activated_time = models.DateField(verbose_name="Дата активации", null=True,
                                    blank=True)
    branch = models.ForeignKey(Branch, verbose_name="Локация",
                               related_name='card_branch')
    activated_in = models.ForeignKey(Branch, verbose_name="Активирована в",
                                     null=True, blank=True,
                                     related_name='card_activated_in')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=1)

    def __str__(self):
        if self.card_number:
            return self.card_number
        else:
            return 0

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


class Image(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя изображения", unique=True)
    image = models.ImageField(upload_to='quests/gallery', null=True, blank=True)
    preview = models.ImageField(upload_to='quests/gallery', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображние"
        verbose_name_plural = "Изображения"

# Квесты
class Quest(models.Model):
    quest = models.CharField(max_length=255, verbose_name="Квест")
    alias = models.SlugField(max_length=255, verbose_name="Псевдоним для обращения", null=True, blank=True, unique=True)
    branch = models.ForeignKey(Branch, verbose_name="Филиал", null=True, blank=True)
    image = models.ImageField(upload_to='quests/main', null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name="Квест запущен")
    description = models.TextField(verbose_name="Описание квеста", default="")
    gallery = models.ManyToManyField(Image)

    def __str__(self):
        return self.quest

    def image_tag(self):
        return '<img style="max-width: 200px; max-height: 200px;" src="%s" />' % self.image.url

    image_tag.short_description = 'Картинка на главной'
    image_tag.allow_tags = True

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


class PromoAction(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    is_active = models.BooleanField(default=True, verbose_name="Акция активна")
    image = models.ImageField(upload_to='promo/%Y/%m/%d', verbose_name="Превью 400 на 600")
    full_image = models.ImageField(upload_to='promo/%Y/%m/%d', verbose_name="Полное изображение", null=True)
    run_date = models.DateTimeField(verbose_name="Дата запуска", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    def image_tag(self):
        return '<img style="max-width: 200px; max-height: 200px;" src="%s" />' % self.image.url

    image_tag.short_description = 'Изображение акции'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"