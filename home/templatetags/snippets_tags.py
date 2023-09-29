from ..snippets.contact_info import ContactInfo

from django import template

register = template.Library()


@register.simple_tag()
def get_contact_info():
    contact_info = ContactInfo.objects.first()
    return contact_info
