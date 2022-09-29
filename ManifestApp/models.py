from secrets import choice
from django.db import models

# Create your models here.
class NodeData(models.Model):

    VSN = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    tags = models.ManyToManyField("Tag")
    gps_lat = models.FloatField() # may be optional
    gps_lan = models.FloatField() # may be optional

    def __str__(self):
         return self.VSN


class Hardware(models.Model):

    cname = models.CharField(max_length=30)
    hw_model = models.CharField(max_length=30)
    hw_version = models.CharField(max_length=30)
    sw_version = models.CharField(max_length=30)
    datasheet = models.CharField(max_length=30)
    cpu = models.CharField(max_length=30)
    cpu_ram = models.CharField(max_length=30)
    gpu_ram = models.CharField(max_length=30)
    shared_ram = models.CharField(max_length=30)
    capabilities = models.ManyToManyField("Capability")

    def __str__(self):
         return self.cname

class Capability(models.Model):

    capability = models.CharField(max_length=30)


class Compute(models.Model):

    ZONE_CHOICES = (
    ('core','core'),
    ('detector', 'detector'),
)

    node = models.ForeignKey(NodeData, on_delete=models.CASCADE)
    cname = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    hardware_id = models.CharField(max_length=30)
    zone = models.CharField(max_length=30, choices=ZONE_CHOICES) # single value & drop down

    def __str__(self):
        return "%s - %s" % (self.node, self.name)


class Sensor(models.Model):
    node = models.ForeignKey(NodeData, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cname = models.CharField(max_length=30)
    labels = models.ManyToManyField("Label")

    def __str__(self):
        return "%s - %s" % (self.node, self.name)


class Resource(models.Model):
    node = models.ForeignKey(NodeData, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s" % (self.node, self.name)


class Tag(models.Model):
    tag = models.CharField(max_length=30) #forest, mountain, mobile

    def __str__(self):
        return self.tag


class Label(models.Model):
    label = models.CharField(max_length=30)

    def __str__(self):
        return self.label