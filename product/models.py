from django.db import models

from e_n_n.models import ElectronicNetworkNode


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название продукта')
    model = models.CharField(max_length=100, verbose_name='модель продукта')
    date = models.DateField(verbose_name='дата выхода продукта на рынок')
    owner = models.ForeignKey(ElectronicNetworkNode, on_delete=models.CASCADE, verbose_name='владелец')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'