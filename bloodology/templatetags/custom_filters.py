from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def truncate_html(content, chars):
    content = strip_tags(content)  # Removes HTML tags
    if len(content) > chars:
        return content[:chars] + "..."
    return content