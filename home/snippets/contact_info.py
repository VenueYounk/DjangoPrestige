from django.db import models
from wagtail.admin.panels import FieldPanel


class ContactInfo(models.Model):
    main_phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Основной номер телефона"
    )
    second_phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Дополнительный номер телефона",
    )
    email = models.EmailField(verbose_name="Почта")

    adress = models.CharField(
        verbose_name="Адрес", blank=True, null=True, max_length=255
    )
    vk_link = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Ссылка на VK"
    )
    telegram_link = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Ссылка на Telegram"
    )
    whatsapp_link = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Ссылка на WhatsApp"
    )

    panels = [
        FieldPanel("main_phone_number"),
        FieldPanel("second_phone_number"),
        FieldPanel("adress"),
        FieldPanel("vk_link"),
        FieldPanel("telegram_link"),
        FieldPanel("whatsapp_link"),
        FieldPanel("email"),
    ]

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"

    def __str__(self):
        return f"Контакты"
