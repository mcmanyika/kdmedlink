# Generated by Django 3.0.4 on 2020-03-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_ajax', '0008_auto_20200313_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_staff',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='t_staff',
            name='lname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]