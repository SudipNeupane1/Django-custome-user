
from rest_framework import serializers
from .models import Author

class AccountSerializer(serializers.ModelSerialize):

    class Meta:
        fields=()
        model = Author
        