# Generated by Django 2.2.3 on 2019-07-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('admin_', '0005_auto_20190722_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagiaire',
            name='S_Image',
            field=models.ImageField(blank=True, default='stagiaire/téléchargement.png', null=True, upload_to='=stagiaire'),
        ),
    ]
