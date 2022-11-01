from django.contrib.auth.models import *
from .models import *
from rest_framework.generics import ListCreateAPIView
from .api.serializers import NodeSerializer
from django.http import HttpResponse

def index(request):
    return HttpResponse('SAGE Beekeeper-Manifest')

class NodeList(ListCreateAPIView):

    queryset = NodeData.objects.all().order_by("VSN")
    serializer_class = NodeSerializer

    def get_queryset(self):
        queryset = NodeData.objects.all().order_by("VSN")
        if 'VSN' in self.request.GET:
            return queryset.filter(VSN=self.request.GET['VSN'])
        return queryset