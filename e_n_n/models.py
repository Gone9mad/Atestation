from datetime import datetime
from django.db import models
from typing import List

NULLABLE = {'null': True, 'blank': True}


class ElectronicNetworkNode(models.Model):
    NODE_TYPES = [(0, 0), (1, 1), (2, 2)]

    name = models.CharField(max_length=100, unique=True, verbose_name='название')
    supplier = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, **NULLABLE)
    node_type = models.IntegerField(choices=NODE_TYPES, verbose_name='Иерархическая позиция')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'
        ordering: List[str] = ['node_type']

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = datetime.now()
        return super().save(*args, **kwargs)



