from dataclasses import fields
from django.contrib import admin
from .models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
class ResourceInline(NestedStackedInline):
    model = Resource
    extra = 0
    fk_name = 'node'

class ComputeSensorInline(NestedStackedInline):
    model = ComputeSensor
    extra = 0
    fk_name = 'scope'

class ComputeInline(NestedStackedInline):
    model = Compute
    extra = 1
    fk_name = 'node'
    inlines = [ComputeSensorInline]

class NodeSensorInline(NestedStackedInline):
    model = NodeSensor
    extra = 0
    fk_name = 'node'

class NodeMetaData(NestedModelAdmin):

    # display in admin panel
    list_display = ('vsn', 'name','gps_lat', 'gps_lon', 'get_tags')

    fieldsets = (
        (None, {"fields": ("vsn", "name", "tags")}),
        ("Location", {"fields": ("gps_lat", "gps_lon")}),
    )

    @admin.display(description='Tags')
    def get_tags(self, obj):
        return ", ".join([t.tag for t in obj.tags.all()])

    inlines = [
        ComputeInline,
        NodeSensorInline,
        ResourceInline
    ]


admin.site.register(NodeData, NodeMetaData)
admin.site.register(Label)
admin.site.register(Tag)
admin.site.register(ComputeHardware)
admin.site.register(SensorHardware)
admin.site.register(ResourceHardware)
admin.site.register(Capability)
