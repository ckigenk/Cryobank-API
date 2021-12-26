from rest_framework import serializers
from .models import Samples


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samples
        fields = '__all__'
