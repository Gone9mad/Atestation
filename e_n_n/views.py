from typing import List
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from e_n_n.models import ElectronicNetworkNode
from e_n_n.serializers import ENNCreateSerializers, ENNListSerializer, ENNSerializer


class ENNCreateAPIView(CreateAPIView):
    model: models.Model = ElectronicNetworkNode
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ENNCreateSerializers


class ENNListAPIView(ListAPIView):

    model = ElectronicNetworkNode
    queryset = ElectronicNetworkNode.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ENNListSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ["contact__country", ]


class ENNAPIView(RetrieveUpdateDestroyAPIView):

    model = ElectronicNetworkNode
    queryset = ElectronicNetworkNode.objects.all()
    serializer_class = ENNSerializer
    permission_classes = [permissions.IsAuthenticated,]
