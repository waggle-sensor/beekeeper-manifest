from .models import *
from rest_framework import serializers

class NodeSerializer(serializers.ModelSerializer):
    computes = serializers.StringRelatedField(many=True)
    sensors = serializers.StringRelatedField(many=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = NodeData
        fields = ['VSN', 'name', 'tags', 'computes', 'sensors']