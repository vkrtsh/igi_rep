from django import template

register = template.Library()


@register.filter
def truncate_to_first_sentence(value):
    if value:
        return value.split('.')[0] + '.'
    return value
