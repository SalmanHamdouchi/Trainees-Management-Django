# Generated by Django 2.2.3 on 2019-07-22 09:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('admin_', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='A_Image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='admin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stagiaire',
            name='S_Image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='=stagiaire'),
            preserve_default=False,
        ),
    ]
