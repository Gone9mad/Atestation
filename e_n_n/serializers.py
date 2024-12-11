from django.db import models
from rest_framework import serializers
from typing import List, Tuple, Dict

from contacts.models import Contacts
from contacts.serializers import ContactsSerializers
from e_n_n.models import ElectronicNetworkNode


class ENNCreateSerializers(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(required=False, queryset=ElectronicNetworkNode.objects.all(), slug_field='name')
    contacts = ContactsSerializers(required=False)

    class Meta:
        model = ElectronicNetworkNode
        read_only_fields = ('id', 'debt', 'date')
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._contacts = self.initial_data.pop('contacts', {})
        #self.initial_data['node_type'] = level_detection(self.initial_data)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data: dict) -> ElectronicNetworkNode:

        node: ElectronicNetworkNode = ElectronicNetworkNode.objects.create(**validated_data)
        node.save()

        contacts = Contacts.objects.create(
            node=node,
            email=self._contacts.get('email', None),
            country=self._contacts.get('country', None),
            city=self._contacts.get('city', None),
            street=self._contacts.get('street', None),
            home=self._contacts.get('home', None)
        )
        contacts.save()

        return node


class ENNListSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(queryset=ElectronicNetworkNode.objects.all(), slug_field='name')
    contacts = ContactsSerializers()

    class Meta:

        model = ElectronicNetworkNode
        fields: List[str] = ['id', 'name', 'node_type', 'supplier', 'debt', 'contacts']


class ENNSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(required=False, queryset=ElectronicNetworkNode.objects.all(), slug_field='name')
    contacts = ContactsSerializers(required=False)

    class Meta:

        model = ElectronicNetworkNode
        fields = '__all__'
        read_only_fields: Tuple[str, ...] = ('id', 'debt', 'date', 'node_type')

    def is_valid(self, *, raise_exception=False):

        self._contacts = self.initial_data.pop('contacts', {})
        if 'supplier' in self.initial_data:
            self.initial_data['node_type'] = level_detection(self.initial_data)
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        super().save()

        if self._contacts != {}:
            self.instance.contacts = self.update(self.instance.contacts, self._contacts)

        return self.instance


def level_detection(kwargs: dict) -> int:
    node_type: int = 0
    if kwargs["supplier"] is None:
        return node_type

    supplier: ElectronicNetworkNode = ElectronicNetworkNode.objects.get(name=kwargs["supplier"])

    for i in range(2):
        node_type += 1
        if supplier.supplier is None:
            return node_type
        supplier = supplier.supplier

    raise Exception("Incorrect links in the hierarchical system")
