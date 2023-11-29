from django import template
from django.db.models.fields.files import FieldFile


register = template.Library()


@register.simple_tag
@register.filter()
def mediapath(data: FieldFile) -> str:
    url = '{{ object.image|mediapath }}'

    return data.url if data else '#'

