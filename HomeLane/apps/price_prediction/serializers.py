from rest_framework import serializers

from .models import HomeLane


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeLane
        fields = ('word',)
