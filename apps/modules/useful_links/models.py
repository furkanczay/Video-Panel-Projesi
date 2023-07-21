from django.db import models
from apps.core.abstracts import AbstractDatesModel
from apps.core.models import Users
from django.utils.translation import gettext_lazy as _
class UsefulLinks(AbstractDatesModel):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Faydalı Link'
        verbose_name_plural = 'Faydalı Linkler'
        ordering = ['-created_on']
        db_table = 'useful_links'
        default_permissions = (
            _('add'), _('change'), _('delete'), _('view')
        )
        permissions = (
            ('useful_links_view', _('Faydalı Linkleri Görüntüle')),
            ('useful_links_add', _('Faydalı Link Ekle')),
            ('useful_links_edit', _('Faydalı Link Düzenle')),
            ('useful_links_delete', _('Faydalı Link Sil')),
        )