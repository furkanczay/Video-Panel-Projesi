from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractDatesModel(models.Model):
    created_on = models.DateTimeField(_('Oluşturulma Tarihi'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Güncellenme Tarihi'), auto_now=True)

    class Meta:
        abstract = True
