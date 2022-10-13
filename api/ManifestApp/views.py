from django.contrib.auth.models import *
from .models import *
from rest_framework import viewsets
from .serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):

    # API endpoint that allows nodes to be viewed or edited.
    queryset = NodeData.objects.all().order_by('VSN')
    serializer_class = NodeSerializer