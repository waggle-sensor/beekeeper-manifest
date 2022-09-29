from django.contrib import admin
from .models import *

# Register your models here.

class ComputeInline(admin.StackedInline):
    model = Compute

class SensorInline(admin.StackedInline):
    model = Sensor

class ResourceInline(admin.StackedInline):
    model = Resource

class NodeMetaData(admin.ModelAdmin):
    inlines = [
        ComputeInline,
        SensorInline,
        ResourceInline,
    ]

admin.site.register(NodeData, NodeMetaData)
admin.site.register(Label)
admin.site.register(Tag)