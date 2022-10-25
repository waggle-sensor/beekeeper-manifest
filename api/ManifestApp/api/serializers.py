from dataclasses import fields
from ..models import *
from collections import defaultdict
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class HardwareSerializer(serializers.ModelSerializer):
    capabilities = serializers.StringRelatedField(many=True)

    class Meta:
        model = Hardware
        fields = ('cname', 'hw_model', 'hw_version', 'sw_version', 'datasheet', 'cpu', 'cpu_ram', 'gpu_ram', 'shared_ram', 'capabilities', )

class NodeSerializer(WritableNestedModelSerializer):
    computes = HardwareSerializer(many=True)
    resources = HardwareSerializer(many=True)
    tags = serializers.StringRelatedField(many=True)
    sensors = serializers.SerializerMethodField("get_sensors")

    def get_sensors(self, request):
        node_id = [node.id for node in NodeData.objects.all()]
        compute_id = []
        sensor_cname = []
        sensor = []

        # collect sensors from NodeSensor & ComputeSensor
        for n in node_id:
            compute_id.extend(c.id for c in Compute.objects.filter(node__id=n))
            sensor_cname.extend(s.cname for s in NodeSensor.objects.filter(node__id=n))

        for c in compute_id:
                sensor_cname.extend(s.cname for s in ComputeSensor.objects.filter(scope__id=c))

        for s_c in sensor_cname:
            for h in Hardware.objects.filter(cname=s_c):
                cap = h.capabilities

                sensor_dict = defaultdict()
                sensor_dict["cname"] = h.cname
                sensor_dict["hw_model"] = h.hw_model
                sensor_dict["hw_version"] = h.hw_version
                sensor_dict["sw_version"] = h.sw_version
                sensor_dict["datasheet"] = h.datasheet
                sensor_dict["datasheet"] = h.datasheet
                sensor_dict["cpu"] = h.cpu
                sensor_dict["cpu_ram"] = h.cpu_ram
                sensor_dict["gpu_ram"] = h.gpu_ram
                sensor_dict["shared_ram"] = h.shared_ram
                sensor_dict["capabilities"] = ["TODO"]

                sensor.append(sensor_dict)

        return sensor

    class Meta:
        model = NodeData
        fields = ('VSN', 'name', 'tags', 'computes', 'sensors', 'resources', )