from django.db import models

# Nodes
class NodeData(models.Model):
    vsn = models.CharField("VSN", max_length=30, unique="True")
    name = models.CharField(max_length=30)
    tags = models.ManyToManyField("Tag", blank=True)
    computes = models.ManyToManyField("ComputeHardware", through="Compute", related_name="computes")
    resources = models.ManyToManyField("ResourceHardware", through="Resource", related_name="resources")
    gps_lat = models.FloatField("Latitude", blank=True, null=True)
    gps_lon = models.FloatField("Longitude", blank=True, null=True)

    def __str__(self):
         return self.vsn

    class Meta:
        verbose_name_plural = "Nodes"

# Hardwares
class CommonHardware(models.Model):
    hardware = models.CharField(max_length=100)
    hw_model = models.CharField(max_length=30, blank=True)
    hw_version = models.CharField(max_length=30, blank=True)
    sw_version = models.CharField(max_length=30, blank=True)
    datasheet = models.CharField(max_length=250, default="<url>", blank=True)
    capabilities = models.ManyToManyField("Capability", blank=True)

    class Meta:
        abstract = True

class ComputeHardware(CommonHardware):
    cpu = models.CharField(max_length=30, blank=True)
    cpu_ram = models.CharField(max_length=30, blank=True)
    gpu_ram = models.CharField(max_length=30, blank=True)
    shared_ram = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.hardware

    class Meta:
        verbose_name_plural = "Compute Hardwares"

class ResourceHardware(CommonHardware):

    def __str__(self):
        return self.hardware

    class Meta:
        verbose_name_plural = "Resource Hardwares"

class SensorHardware(CommonHardware):

    def __str__(self):
        return self.hardware

    class Meta:
        verbose_name_plural = "Sensor Hardwares"

# Capability for Compute Hardwares
class Capability(models.Model):
    capability = models.CharField(max_length=30)

    def __str__(self):
         return self.capability

    class Meta:
        verbose_name_plural = "Capabilities"

# Compute Hardwares attached to a Node
class Compute(models.Model):

    ZONE_CHOICES = (
        ("core", "core"),
        ("agent", "agent"),
        ("detector", "detector"),
        ("shield", "shield")
    )

    node = models.ForeignKey(NodeData, on_delete=models.CASCADE, blank=True)
    hardware = models.ForeignKey(ComputeHardware, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=30, default="", blank=True)
    serial_no = models.CharField(max_length=30, default="<MAC ADDRESS>", blank=True)
    zone = models.CharField(max_length=30, choices=ZONE_CHOICES, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Compute"

# Sensor hardwares
class CommonSensor(models.Model):
    hardware = models.ForeignKey(SensorHardware, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=30, blank=True)
    labels = models.ManyToManyField("Label", blank=True)

    class Meta:
        abstract = True


class NodeSensor(CommonSensor):
    node = models.ForeignKey(NodeData, on_delete=models.CASCADE, blank=True)
    scope = models.CharField(max_length=30, default="global", blank=True)


class ComputeSensor(CommonSensor):
    scope = models.ForeignKey(Compute, on_delete=models.CASCADE, blank=True)

# Resource hardwares attached to a node
class Resource(models.Model):
    node = models.ForeignKey(NodeData, on_delete=models.CASCADE, blank=True)
    hardware = models.ForeignKey(ResourceHardware, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

# Tags for nodes
class Tag(models.Model):
    tag = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.tag

    def natural_key(self):
        return self.tag

# label for sensors
class Label(models.Model):
    label = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.label

    def natural_key(self):
        return self.label
