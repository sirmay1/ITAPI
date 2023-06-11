from .models import Tech
from rest_framework import serializers


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ('id', 'name', 'paradigm', 'category', 'detail')
