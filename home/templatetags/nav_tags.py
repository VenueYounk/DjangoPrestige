from django import template

from home.models import ServicesCategory

register = template.Library()


@register.simple_tag()
def get_services_menu():
    """
    Retrieves the services menu.

    Returns:
        dict: A dictionary containing the services menu. The keys of the dictionary are the root categories of the services menu, and the values are the corresponding child categories.
    """
    roots = ServicesCategory.objects.all()
    result = {}
    for root in roots:
        result[root] = root.get_children()
    return result
