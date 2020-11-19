from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class  Participant(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    educational_institution = models.CharField(max_length=150,verbose_name='Наименование учебного учреждения')
    phone = models.CharField(max_length=11, verbose_name='Телефон', unique=True, validators = [RegexValidator(regex=r'\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d',
                                                                                                              message='Телефон введен в неверном формате',
                                                                                                              code='invalid_phonenumber')])
    email = models.CharField(max_length=50, verbose_name='E-mail', unique=True)

    def __str__(self):
        return f"{self.full_name}"