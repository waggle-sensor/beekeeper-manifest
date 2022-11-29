from ..models import *
import csv


def run():
    with open('ManifestApp/data/hardware.csv') as file:
        reader = csv.DictReader(file)

        Hardware.objects.all().delete()

        for row in reader:
            print(row)

            hardware = Hardware(hardware=row["hardware"].strip(),
                        hw_model=row["hw_model"].strip(),
                        hw_version=row["hw_version"].strip(),
                        sw_version=row["sw_version"].strip(),
                        datasheet=row["datasheet"].strip(),
                        cpu=row["cpu"].strip(),
                        cpu_ram=row["cpu_ram"].strip(),
                        gpu_ram=row["gpu_ram"].strip(),
                        shared_ram=bool(row["shared_ram"].strip())
                        )
            hardware.save()

            # Create Capabilitiy object only if hardware.csv/capabilities column has value and the val does not exist in current Capability model
            if len(row["capabilities"].strip()) > 0:
                for c in row["capabilities"].split(","):
                    if not Capability.objects.filter(capability=c):
                        Capability.objects.create(capability=c)
                    capability = Capability.objects.get(capability=c)
                    hardware.capabilities.add(capability)



