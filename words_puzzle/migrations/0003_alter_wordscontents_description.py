# Generated by Django 3.2.6 on 2022-05-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words_puzzle', '0002_rename_name_wordscontents_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordscontents',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
