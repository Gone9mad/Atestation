from rest_framework import serializers
from typing import List

from contacts.models import Contacts


class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields: List[str] = ['email', 'country', 'city', 'street', 'home']
