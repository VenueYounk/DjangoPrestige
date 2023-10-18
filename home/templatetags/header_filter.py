from django import template
from bs4 import BeautifulSoup

register = template.Library()


@register.filter()
def hsplit(content):
    soup = BeautifulSoup(str(content), "html.parser")
    h2_tags = soup.find_all("h2")
    h2_data = []

    for h2 in h2_tags:
        h2_text = h2.get_text()
        h2_id = h2.get("id")
        h2_data.append({"value": h2_text, "id": h2_id})

    return h2_data
