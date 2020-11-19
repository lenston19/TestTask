# Generated by Django 3.1.3 on 2020-11-18 22:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Participation', '0003_auto_20201119_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_phonenumber', message='Телефон введен в неверном формате', regex='\\+?\\d{1,3}?[- .]?\\(?(?:\\d{2,3})\\)?[- .]?\\d\\d\\d[- .]?\\d\\d\\d\\d')], verbose_name='Телефон'),
        ),
    ]