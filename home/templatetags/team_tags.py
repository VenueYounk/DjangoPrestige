from django import template
from ..models import Lawyer
from wagtail.models import Page

register = template.Library()


@register.simple_tag()
def get_team(page: Page):
    if page.__class__.__name__ == "ServicesPage":
        category = page.get_parent()
        lawyers = Lawyer.objects.filter(tags=category)

        return {"lawyers": lawyers, "label": "Специалисты в этой области"}
    else:
        lawyers = Lawyer.objects.filter(is_first_page=True)
        return {"lawyers": lawyers, "label": "Команда"}
