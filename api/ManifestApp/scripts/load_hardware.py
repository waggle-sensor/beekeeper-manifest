from ..models import *
import csv


def run():
    with open('ManifestApp/data/hardware.csv') as file:
        reader = csv.DictReader(file)

        ComputeHardware.objects.all().delete()
        SensorHardware.objects.all().delete()
        ResourceHardware.objects.all().delete()
        Capability.objects.all().delete()

        for row in reader:
            print(row)

            if row["hardware_type"] == "compute":
                hardware = ComputeHardware.objects.create(hardware=row["hardware"].strip(),
                            hw_model=row["hw_model"].strip(),
                            hw_version=row["hw_version"].strip(),
                            datasheet=row["datasheet"].strip(),
                            cpu=row["cpu"].strip(),
                            cpu_ram=row["cpu_ram"].strip(),
                            gpu_ram=row["gpu_ram"].strip(),
                            shared_ram=bool(row["shared_ram"].strip())
                            )

                # Create Capabilitiy object only if hardware.csv/capabilities column has value and the val does not exist in current Capability model
                if len(row["capabilities"].strip()) > 0:
                    for c in row["capabilities"].split(","):
                        c = c.strip()
                        if not Capability.objects.filter(capability=c):
                            Capability.objects.create(capability=c)
                        capability = Capability.objects.get(capability=c)
                        hardware.capabilities.add(capability)

            elif row["hardware_type"] == "sensor":
                SensorHardware.objects.create(hardware=row["hardware"].strip(),
                            hw_model=row["hw_model"].strip(),
                            hw_version=row["hw_version"].strip(),
                            datasheet=row["datasheet"].strip()
                            )

            elif row["hardware_type"] == "resource":
                ResourceHardware.objects.create(hardware=row["hardware"].strip(),
                            hw_model=row["hw_model"].strip(),
                            hw_version=row["hw_version"].strip(),
                            datasheet=row["datasheet"].strip()
                            )