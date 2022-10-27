from django.contrib.auth.models import *
from .models import *
from rest_framework.generics import ListCreateAPIView
from .api.serializers import NodeSerializer

def index(request):
    return HttpResponse('SAGE Beekeeper-Manifest')

class NodeList(ListCreateAPIView):

    queryset = NodeData.objects.all().order_by("VSN")
    serializer_class = NodeSerializer