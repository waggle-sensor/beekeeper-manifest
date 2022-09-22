from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(NodeData)
admin.site.register(Compute)
admin.site.register(Sensor)
admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(Label)
