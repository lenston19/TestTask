# Generated by Django 3.1.3 on 2020-11-18 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Participation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='educational_institution',
            field=models.CharField(max_length=150, verbose_name='Наименование учебного учреждения'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.CharField(max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
    ]