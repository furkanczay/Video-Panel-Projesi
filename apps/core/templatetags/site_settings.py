from django import template
from apps.manager.models import GeneralSettings, LinksSettings

register = template.Library()


@register.simple_tag()
def get_general_settings():
    general_settings = GeneralSettings.objects.first()
    return general_settings


@register.simple_tag()
def get_links_settings():
    links_settings = LinksSettings.objects.first()
    return links_settings
