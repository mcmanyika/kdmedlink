# Generated by Django 2.1.7 on 2020-02-05 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_ajax', '0002_t_calls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_calls',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='t_calls',
            name='updated',
        ),
    ]
