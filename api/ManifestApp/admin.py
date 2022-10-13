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
class SensorInline(admin.StackedInline):
    model = Sensor

class ComputeInline(admin.StackedInline):
    model = Compute

    inlines = [SensorInline]

class ResourceInline(admin.StackedInline):
    model = Resource

class NodeMetaData(admin.ModelAdmin):
    actions = [export_as_json]

    # display in admin panel
    list_display = ('VSN', 'name', 'gps_lat', 'gps_lan', 'get_tags', 'get_computes')

    @admin.display(description='Tags')
    def get_tags(self, obj):
        return ", ".join([t.tag for t in obj.tags.all()])

    @admin.display(description='Computes')
    def get_computes(self, obj):
        return ", ".join([c.cname for c in obj.computes.all()])

    inlines = [
        ComputeInline,
        ResourceInline
    ]

admin.site.register(NodeData, NodeMetaData)
admin.site.register(Label)
admin.site.register(Tag)
admin.site.register(Hardware)
admin.site.register(Capability)
