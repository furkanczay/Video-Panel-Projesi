from django.db import models
from apps.core.models import Users, AbstractDatesModel
from django.utils.translation import gettext_lazy as _

COLORS = [
    ('red', _('Kırmızı')),
    ('blue', _('Mavi')),
    ('green', _('Yeşil')),
    ('orange', _('Turuncu')),
    ('gray', _('Gri'))
]


class TicketCategories(AbstractDatesModel):
    name = models.CharField(_('Kategori Adı'), max_length=150)
    color = models.CharField(_('Kategori Renk'), max_length=20, choices=COLORS, default='red')

    class Meta:
        db_table = 'ticket_categories'
        verbose_name = _('Destek Talebi Kategorisi')
        verbose_name_plural = _('Destek Talebi Kategorileri')

    def __str__(self):
        return self.name


class TicketStatuses(AbstractDatesModel):
    name = models.CharField(_('Durum Adı'), max_length=150)
    color = models.CharField(_('Durum Renk'), max_length=20, choices=COLORS, default='green')

    class Meta:
        db_table = 'ticket_statuses'
        verbose_name = _('Destek Talebi Durumu')
        verbose_name_plural = _('Destek Talebi Durumları')

    def __str__(self):
        return self.name


class TicketPriorities(AbstractDatesModel):
    name = models.CharField(_('Öncelik Adı'), max_length=150)
    color = models.CharField(_('Öncelik Renk'), max_length=20, choices=COLORS, default='blue')

    class Meta:
        db_table = 'ticket_priorities'
        verbose_name = _('Destek Talebi Önceliği')
        verbose_name_plural = _('Destek Talebi Öncelikleri')

    def __str__(self):
        return self.name


class Ticket(AbstractDatesModel):
    subject = models.CharField(_('Konu'), max_length=150)
    content = models.TextField(_('İçerik'))
    status = models.ForeignKey(TicketStatuses, on_delete=models.SET_DEFAULT, related_name='status_tickets',
                               default=1, verbose_name=_('Durum'))
    priority = models.ForeignKey(TicketPriorities, on_delete=models.SET_DEFAULT, related_name='priority_tickets',
                                 default=1, verbose_name=_('Öncelik'))
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_tickets', verbose_name=_('Kullanıcı'))
    agent = models.ForeignKey(Users, on_delete=models.SET_NULL, related_name='agent_tickets', null=True, blank=True,
                              verbose_name=_('Görevli'))
    category = models.ForeignKey(TicketCategories, on_delete=models.SET_DEFAULT, related_name='category_tickets',
                                 default=1, verbose_name=_('Kategori'))
    completed_on = models.DateTimeField(null=True, blank=True, verbose_name=_('Tamamlanma Tarihi'))

    class Meta:
        db_table = 'tickets'
        verbose_name = _('Destek Talebi')
        verbose_name_plural = _('Destek Talepleri')

    def __str__(self):
        return self.user.get_full_name()


class TicketMessages(AbstractDatesModel):
    content = models.TextField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='ticket_comments',
                             verbose_name=_('Kullanıcı'))
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments',
                               verbose_name=_('Destek Talebi'))

    class Meta:
        db_table = 'ticket_messages'
        verbose_name = _('Destek Talebi Mesajı')
        verbose_name_plural = _('Destek Talebi Mesajları')

    def __str__(self):
        return self.user.get_full_name()
