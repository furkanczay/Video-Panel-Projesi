# Generated by Django 4.2.2 on 2023-06-25 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_videos_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='instructor',
            field=models.ForeignKey(default=1, limit_choices_to={'groups__name': 'Eğitmen'}, on_delete=django.db.models.deletion.CASCADE, related_name='instructor_classrooms', to=settings.AUTH_USER_MODEL, verbose_name='Eğitmen'),
        ),
    ]