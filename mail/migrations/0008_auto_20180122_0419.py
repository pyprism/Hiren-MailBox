# Generated by Django 2.0.1 on 2018-01-22 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_auto_20180119_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='received_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='mail',
            name='sane_body',
            field=models.TextField(null=True),
        ),
    ]
