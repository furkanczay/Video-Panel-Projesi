from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'apps.core':  # Uygulama adını buraya girin
        Group.objects.get_or_create(name='Öğrenci')  # Grupları burada oluşturun
        Group.objects.get_or_create(name='Eğitmen')
        Group.objects.get_or_create(name='Personel')
        Group.objects.get_or_create(name='Yönetici')
