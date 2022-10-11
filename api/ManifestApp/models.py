from django.db import models


# Create your models here.

# NodeData
class NodeData(models.Model):

    VSN = models.CharField(max_length=30, unique="True")
    name = models.CharField(max_length=30)
    tags = models.ManyToManyField("Tag")
    computes = models.ManyToManyField("Hardware", through="Compute")
    gps_lat = models.FloatField(blank=True)
    gps_lan = models.FloatField(blank=True)

    def __str__(self):
         return self.VSN

# Hardware
class Hardware(models.Model):

    cname = models.CharField(max_length=30)
    hw_model = models.CharField(max_length=30, blank=True)
    hw_version = models.CharField(max_length=30, blank=True)
    sw_version = models.CharField(max_length=30, blank=True)
    datasheet = models.CharField(max_length=30, default='<url>', blank=True)
    cpu = models.CharField(max_length=30, blank=True)
    cpu_ram = models.CharField(max_length=30, blank=True)
    gpu_ram = models.CharField(max_length=30, blank=True)
    shared_ram = models.BooleanField(default=False, blank=True)
    capabilities = models.ManyToManyField("Capability", blank=True)

    def __str__(self):
         return self.cname

# Capability
class Capability(models.Model):

    capability = models.CharField(max_length=30)

    def __str__(self):
         return self.capability

# Compute
class Compute(models.Model):

    ZONE_CHOICES = (
        ('core','core'),
        ('detector', 'detector'),
        ('zone', 'zone')
    )

    node = models.ForeignKey(NodeData, on_delete=models.CASCADE, related_name='compute_nodedata')
    cname = models.ForeignKey(Hardware, on_delete=models.CASCADE, related_name='compute_cname')
    sensors = models.ManyToManyField("Hardware", through="Sensor", related_name='compute_sensors')
    name = models.CharField(max_length=30, default='')
    serial_no = models.CharField(max_length=30, default='<MAC ADDRESS>')
    zone = models.CharField(max_length=30, choices=ZONE_CHOICES)

    class Meta:
        unique_together = ['node', 'cname']

    def __str__(self):
        return self.name

# Sensor
class Sensor(models.Model):
    # should change node into compute
    node = models.ForeignKey(Compute, on_delete=models.CASCADE, related_name='sensor_node')
    cname = models.ForeignKey(Hardware, on_delete=models.CASCADE, related_name='sensor_cname')
    name = models.CharField(max_length=30)
    labels = models.ManyToManyField("Label", blank=True)

    def __str__(self):
        return self.name

# Resource
class Resource(models.Model):
    node = models.ForeignKey(NodeData, on_delete=models.CASCADE)
    cname = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Tag
class TagManager(models.Manager):
    def get_by_natural_key(self, tag):
        return self.get(tag=tag)

class Tag(models.Model):
    tag = models.CharField(max_length=30, unique="True")

    objects = TagManager()

    def __str__(self):
        return self.tag

    def natural_key(self):
        return self.tag

# Label
class Label(models.Model):
    label = models.CharField(max_length=30)

    def __str__(self):
        return self.label