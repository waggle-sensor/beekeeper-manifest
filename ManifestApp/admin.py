from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Compute)
# admin.site.register(Sensor)
# admin.site.register(Resource)
# admin.site.register(Tag)
# admin.site.register(Label)


class ComputeInline(admin.StackedInline):
    model = Compute

class SensorInline(admin.StackedInline):
    model = Sensor

class ResourceInline(admin.StackedInline):
    model = Resource

# class TagInline(admin.StackedInline):
#     model = Tag

# class LabelInline(admin.StackedInline):
#     model = Label

class NodeMetaData(admin.ModelAdmin):
    inlines = [
        ComputeInline,
        SensorInline,
        ResourceInline,
    ]

admin.site.register(NodeData, NodeMetaData)