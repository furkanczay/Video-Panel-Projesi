from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from apps.core.models import Videos
from discord_webhook import DiscordWebhook
from django.conf import settings


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'apps.core':  # Uygulama adını buraya girin
        Group.objects.get_or_create(name='Öğrenci')  # Grupları burada oluşturun
        Group.objects.get_or_create(name='Eğitmen')
        Group.objects.get_or_create(name='Personel')
        Group.objects.get_or_create(name='Yönetici')


@receiver(post_save, sender=Videos)  # VideoModel, video modelinizi temsil eden model adı ile değiştirin
def send_discord_message(sender, instance, created, **kwargs):
    webhook_url = settings.WEBHOOK_URL
    instructor = instance.instructor.get_full_name()
    video_title = instance.title
    video = instance.video_file
    if created:
        message = f"{instructor}, {video_title} isminde yeni bir video paylaştı\nizlemek için: {video.url}"
        webhook = DiscordWebhook(url=webhook_url, content=message)
        webhook.execute()
