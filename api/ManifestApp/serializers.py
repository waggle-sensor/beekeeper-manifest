from dataclasses import field, fields
from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class ComputeSerializer(serializers.ModelSerializer):
    compute_cname = serializers.StringRelatedField(many=True)
    compute_sensors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Compute
        fields = ('compute_cname', 'compute_sensors',)

class NodeSerializer(WritableNestedModelSerializer):
    computes = ComputeSerializer(many=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = NodeData
        fields = ('VSN', 'name', 'tags', 'computes', )