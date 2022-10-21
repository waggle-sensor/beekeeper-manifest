from dataclasses import field, fields
from statistics import mode
from ..models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class HardwareSerializer(serializers.ModelSerializer):
    capabilities = serializers.StringRelatedField(many=True)

    class Meta:
        model = Hardware
        fields = ('cname', 'hw_model', 'hw_version', 'sw_version', 'datasheet', 'cpu', 'cpu_ram', 'gpu_ram', 'shared_ram', 'capabilities', )

class NodeSerializer(WritableNestedModelSerializer):
    computes = HardwareSerializer(many=True)
    sensors = HardwareSerializer(many=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = NodeData
        fields = ('VSN', 'name', 'tags', 'computes', 'sensors', )