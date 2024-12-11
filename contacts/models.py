from django.db import models

from e_n_n.models import ElectronicNetworkNode


class Contacts(models.Model):
    node = models.OneToOneField(ElectronicNetworkNode, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    home = models.IntegerField(verbose_name='номер дома')

    def __str__(self):
        return f'{self.email} - {self.country} - {self.city} - {self.street} - {self.home}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
