# Generated by Django 3.2.6 on 2021-11-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jcsg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jcsgcontents',
            name='status',
            field=models.CharField(choices=[('READ', 'Read'), ('NOT_READ', 'not read')], default='NOT_READ', max_length=20),
        ),
    ]
