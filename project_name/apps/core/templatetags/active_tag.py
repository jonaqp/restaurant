from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def add_active(context, name, by_path=False):
    request = context["request"]
    if by_path:
        path = name
    else:
        try:
            path = reverse(name)
        except NoReverseMatch:
            path = ''
    if request.path == path:
        return 'active'
    return ''
