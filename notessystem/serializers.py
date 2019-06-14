from rest_framework import serializers
from .models import add
class data(serializers.ModelSerializer):
    class Meta:
        model=add
        fields='__all__'