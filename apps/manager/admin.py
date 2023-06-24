from django.contrib import admin
from .models import GeneralSettings, LinksSettings

admin.site.register(GeneralSettings)
admin.site.register(LinksSettings)
