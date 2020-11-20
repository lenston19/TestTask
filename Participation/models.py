from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class  Participant(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    educational_institution = models.CharField(
        max_length=150,
        verbose_name='Наименование учебного учреждения'
    )
    phone = models.CharField(
        max_length=16,
        verbose_name='Телефон',
        unique=True,
        validators = [RegexValidator(
            regex=r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]',
            message='Телефон введен в неверном формате',
            code='invalid_phonenumber')]
    )
    email = models.CharField(
        max_length=50,
        verbose_name='E-mail',
        unique=True,
        validators = [RegexValidator(
            regex=r'\w[\w\.-]*@\w[\w\.-]+\.\w+',
            message='Email введен в неверном формате',
            code='invalid_email')]
    )

    def __str__(self):
        return f"{self.full_name}"