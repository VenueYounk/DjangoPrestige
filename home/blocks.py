from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import StructBlock, CharBlock, RichTextBlock


class ImageWithCaption(StructBlock):
    caption = CharBlock(
        label="Подпись",
    )
    img = ImageChooserBlock(
        label="Картинка",
    )

    class Meta:
        icon = "image"
        template = "blocks/image_with_caption.html"


class ListBullet(StructBlock):
    header = CharBlock(
        label="Заголовок пункта",
    )
    text = RichTextBlock(
        label="Текст пункта",
    )

    class Meta:
        icon = "list-ul"
        template = "blocks/list_bullet.html"
