from django.db import models
from django.utils.translation import gettext_lazy as _


# ADMIN PANEL SETTINGS MODELS
class GeneralSettings(models.Model):
    site_url = models.URLField(null=True, blank=True, default='http://127.0.0.1:8000/')
    site_description = models.CharField(_('Meta Açıklama'), max_length=255, null=True, blank=True, default='AcunmedyaAkademi Videolar')
    site_keywords = models.CharField(_('Meta Anahtar Kelimeler'), max_length=255, null=True, blank=True,
                                     default='akademi,acunmedyaakademi,acunmedyaakademi videolar')
    site_author = models.CharField(_('Meta Author Metni'), max_length=255, null=True, blank=True,
                                   default='acunmedyaakademi')
    site_copyright = models.CharField(_('Copyright Metni'), max_length=255, null=True, blank=True,
                                      default='AcunMedyaAkademi')
    site_developers = models.CharField(_('Geliştiriciler'), max_length=255, null=True, blank=True, default='Furkan Özay')
    site_version = models.CharField(_('Versiyon'), max_length=50, default='v1.0.0-beta1')
    site_privacy_policy = models.TextField(_('Gizlilik Politikası'), null=True)
    site_terms_of_use = models.TextField(_('Kullanım Şartları'), null=True)

    class Meta:
        db_table = 'general_settings'
        verbose_name = _('Genel Ayarlar')
        verbose_name_plural = _('Genel Ayarlar')

    def __str__(self):
        return str(self.id)


class LinksSettings(models.Model):
    instagram_link = models.CharField(max_length=200, null=True, blank=True)
    youtube_link = models.CharField(max_length=200, null=True, blank=True)
    facebook_link = models.CharField(max_length=200, null=True, blank=True)
    tiktok_link = models.CharField(max_length=200, null=True, blank=True)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'links_settings'
        verbose_name = _('Bağlantı Ayarları')
        verbose_name_plural = _('Bağlantı Ayarları')

    def __str__(self):
        return str(self.id)
