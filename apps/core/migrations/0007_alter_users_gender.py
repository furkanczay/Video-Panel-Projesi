# Generated by Django 4.2.2 on 2023-06-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_generalsettings_delete_linkssettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın'), ('Diğer', 'Diğer')], max_length=6, null=True, verbose_name='Cinsiyet'),
        ),
    ]
