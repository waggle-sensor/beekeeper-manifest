from dataclasses import fields
from django.contrib import admin
from .models import *
from django.core import serializers
from django.http import HttpResponse

# admin page actions
@admin.action(description='Export as JSON')
def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response, use_natural_foreign_keys=True)
    return response

# Register your models here.
class ComputeInline(admin.StackedInline):
    model = Compute

class SensorInline(admin.StackedInline):
    model = Sensor

class ResourceInline(admin.StackedInline):
    model = Resource

class NodeMetaData(admin.ModelAdmin):
    actions = [export_as_json]

    inlines = [
        ComputeInline,
        SensorInline,
        ResourceInline
    ]

admin.site.register(NodeData, NodeMetaData)
admin.site.register(Label)
admin.site.register(Tag)
admin.site.register(Hardware)
admin.site.register(Capability)
