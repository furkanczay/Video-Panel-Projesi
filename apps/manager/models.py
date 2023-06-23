from django.db import models


# ADMIN PANEL SETTINGS MODELS
class GeneralSettings(models.Model):
    site_url = models.URLField(null=True, blank=True, default='127.0.0.1:8000/')
    site_description = models.CharField(max_length=255, null=True, blank=True, default='AcunmedyaAkademi Videolar')
    site_keywords = models.CharField(max_length=255, null=True, blank=True,
                                     default='akademi,acunmedyaakademi,acunmedyaakademi videolar')
    site_author = models.CharField(max_length=255, null=True, blank=True, default='acunmedyaakademi')
    site_copyright = models.CharField(max_length=255, null=True, blank=True, default='AcunMedyaAkademi')
    site_developers = models.CharField(max_length=255, null=True, blank=True, default='Furkan Özay')


class LinksSettings(models.Model):
    instagram_link = models.CharField(max_length=200, null=True, blank=True)
    youtube_link = models.CharField(max_length=200, null=True, blank=True)
    facebook_link = models.CharField(max_length=200, null=True, blank=True)
    tiktok_link = models.CharField(max_length=200, null=True, blank=True)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True)
