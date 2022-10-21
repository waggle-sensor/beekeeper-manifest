from django.contrib.auth.models import *
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from .api.serializers import NodeSerializer

class NodeViewSet(viewsets.ViewSet):

    def list(self, request, format=None):
        node_id = [node.id for node in NodeData.objects.all()]
        VSN = [node.VSN for node in NodeData.objects.all()]
        name = [node.name for node in NodeData.objects.all()]
        gps_lat = [node.gps_lat for node in NodeData.objects.all()]
        gps_lan = [node.gps_lan for node in NodeData.objects.all()]

        compute_id = []
        compute_name = []
        sensor = []
        resource = []

        for n in node_id:
            compute_name.extend(c.name for c in Compute.objects.filter(node__id=n))
            compute_id.extend(c.id for c in Compute.objects.filter(node__id=n))
            sensor.extend(s.name for s in NodeSensor.objects.filter(node__id=n))
            resource.extend(r.name for r in Resource.objects.filter(node__id=n))


        for c in compute_id:
                sensor.extend(s.name for s in ComputeSensor.objects.filter(scope__id=c))

        # for sensors in sensor_id:
        #     for s in sensors:
        #         sensor.append(h.cname for h in Hardware.objects.filter(id =s))

        return Response({
            "VSN": VSN,
            "name": name,
            "gps_lat": gps_lat,
            "gps_lan": gps_lan,
            "Computes": compute_name,
            "Sensor": sensor,
            "Resource": resource,
        })
