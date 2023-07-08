# Generated by Django 4.2.3 on 2023-07-07 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefulLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=255)),
                ('description', models.TextField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Faydalı Link',
                'verbose_name_plural': 'Faydalı Linkler',
                'db_table': 'useful_links',
                'ordering': ['-created_on'],
                'permissions': (('useful_links_view', 'Faydalı Linkleri Görüntüle'), ('useful_links_add', 'Faydalı Link Ekle'), ('useful_links_edit', 'Faydalı Link Düzenle'), ('useful_links_delete', 'Faydalı Link Sil')),
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
    ]
