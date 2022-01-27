"""Edittags file."""
import re
# Django
from django import template
from django.apps import apps
from django.urls import reverse
from django.utils.safestring import mark_safe

get_model = apps.get_model

register = template.Library()


@register.simple_tag
def multiply(a,b):  # noqa:
    return "%.2f" % float(a*float(b))


@register.simple_tag
def checksum(dict):  # noqa:
    suma = 0
    print(dict)
    for key, value in dict:
        suma += float(value['quantity']*float(value['price']))
    return "%.2f" % suma
