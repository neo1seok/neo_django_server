# Generated by Django 3.2.6 on 2021-12-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_rename_contents_diarycontents_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarycontents',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]