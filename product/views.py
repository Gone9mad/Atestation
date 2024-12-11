from rest_framework import viewsets

from product.models import Product
from product.serializers import ProductSerializers


class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
