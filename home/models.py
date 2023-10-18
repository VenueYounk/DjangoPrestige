import os
from .utils import helper

from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.blocks import RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.rich_text import RichText
from .blocks import ImageWithCaption, ListBullet
from bs4 import BeautifulSoup
from transliterate import translit
import re
from modelcluster.fields import ParentalKey, ParentalManyToManyField


for snippets in helper.get_all_snippets(os.path.dirname(__file__)):
    register_snippet(snippets)


class HomePage(Page):
    about_college = RichTextField(
        features=["h2", "bold", "italic"],
        blank=True,
        null=True,
        help_text="Текст о коллегии",
    )
    content_panels = Page.content_panels + [
        FieldPanel("about_college"),
    ]
    max_count = 1
    subpage_types = ["home.Services", "home.TestPage", "home.Lawyers"]


# Модели связанные с услугами


class ServicesCategory(Page):
    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"

    subpage_types = ["home.ServicesPage"]


class Services(Page):
    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"

    subpage_types = ["home.ServicesCategory"]

    max_count = 1


class ServicesPage(Page):
    subtitle = models.CharField(
        max_length=70, verbose_name="Заголовок к призыву", blank=True, null=True
    )
    subtitle_second = models.CharField(
        max_length=70, verbose_name="Подзаголовок к призыву", blank=True, null=True
    )

    content = StreamField(
        [
            (
                "text",
                RichTextBlock(
                    features=["h2", "bold", "italic"],
                    label="Текст",
                    help_text="Основной контент",
                ),
            ),
            (
                "image",
                ImageWithCaption(
                    label="Картинка с подписью",
                ),
            ),
            (
                "quotes",
                RichTextBlock(
                    label="Цитата",
                ),
            ),
            (
                "list",
                StreamBlock(
                    [
                        ("bullet", ListBullet(label="Пункт")),
                    ],
                    label="Список с пунктами",
                ),
            ),
        ],
        use_json_field=True,
        default={},
        verbose_name="Контент страницы",
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("subtitle_second"),
        FieldPanel("content"),
    ]

    parent_page_types = ["home.ServicesCategory"]
    subpage_types = []

    def add_ids_to_h2_tags(self, content):
        soup = BeautifulSoup(str(content), "html.parser")
        h2_tags = soup.find_all("h2")

        new_content = []
        for content in content:
            if content.block_type == "text":
                soup = BeautifulSoup(str(content), "html.parser")
                h2_tags = soup.find_all("h2")
                for h2 in h2_tags:
                    h2_text = h2.get_text()
                    h2_id = translit(h2_text, "ru", reversed=True)
                    h2_id = h2_id.lower().replace(" ", "-")
                    h2_id = re.sub(r"[^a-zA-Z0-9_-]", "", h2_id)
                    h2["id"] = h2_id

                new_content.append(("text", RichText(str(soup))))
            else:
                new_content.append((content.block_type, content.value))

        return new_content

    def save(self, *args, **kwargs):
        # Call the parent save method to save the page
        super().save(*args, **kwargs)
        # Update the page's content by adding IDs to h2 tags
        self.content = self.add_ids_to_h2_tags(self.content)

        # Call the parent save method again to save the updated content
        super().save(*args, **kwargs)


# Модель связывающая адвокатов с делами


# class LawyerServicesCategoryRelationship(models.Model):
#     lawyer = ParentalKey("home.Lawyer", on_delete=models.CASCADE, related_name="lawyer")
#     services_category = ParentalKey(
#         "home.ServicesCategory",
#         on_delete=models.CASCADE,
#         related_name="services_category",
#     )

#     class Meta:
#         unique_together = ("lawyer", "services_category")


# Модели связанные с адвокатами


class Lawyers(Page):
    class Meta:
        verbose_name = "Адвокаты"
        verbose_name_plural = "Адвокатыг"

    max_count = 1
    subpage_types = ["home.Lawyer"]


class Lawyer(Page):
    role = models.CharField(
        max_length=70, verbose_name="Должность", blank=False, null=False
    )
    reg_num = models.CharField(
        max_length=70, verbose_name="Регистрационный номер", blank=False, null=False
    )
    experience = models.CharField(
        max_length=70, verbose_name="Опыт работы", blank=False, null=False
    )

    is_first_page = models.BooleanField(
        default=False,
        verbose_name="Выводить на главную страницу",
    )

    lawyer_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    tags = ParentalManyToManyField("home.ServicesCategory", blank=True)

    short_description = RichTextField(
        features=["h2", "bold", "italic"],
        blank=True,
        null=True,
        help_text="Текст в карточках",
    )

    content = StreamField(
        [
            (
                "text",
                RichTextBlock(
                    features=["h2", "bold", "italic"],
                    label="Текст",
                    help_text="Основной контент",
                ),
            )
        ],
        use_json_field=True,
        default={},
        verbose_name="Контент страницы",
    )

    content_panels = Page.content_panels + [
        FieldPanel("is_first_page"),
        FieldPanel("role"),
        FieldPanel("experience"),
        FieldPanel("reg_num"),
        FieldPanel("lawyer_image"),
        FieldPanel("tags", widget=forms.CheckboxSelectMultiple),
        FieldPanel("short_description"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Адвокат"
        verbose_name_plural = "Адвокаты"

    parent_page_types = ["home.Lawyers"]


class TestPage(Page):
    pass
