from ..models import *
import csv


def run():
    with open('ManifestApp/data/nodedata.csv') as file:
        reader = csv.DictReader(file)

        # skip the data type row
        next(reader)

        NodeData.objects.all().delete()
        Compute.objects.all().delete()
        ComputeSensor.objects.all().delete()
        NodeSensor.objects.all().delete()
        Resource.objects.all().delete()

        for row in reader:
            print(row)

            n = NodeData.objects.create(vsn=row["vsn"].strip(),
                        gps_lat=float(row["gps_lat"].strip() or 0),
                        gps_lon=float(row["gps_lon"].strip() or 0)
                        )

            # add below hardwares to every node:
            # 1. compute-xaviernx
            nx = Hardware.objects.get(hardware="compute-xaviernx")
            n.computes.add(nx)
            Compute.objects.filter(node=n, hardware=nx).update(zone="core")
            Compute.objects.filter(node=n, hardware=nx).update(serial_no=row["node_id"][4:])

            # 2. sensor-bme280-1
            compute = Compute.objects.get(node=n, hardware=nx)
            ComputeSensor.objects.create(scope=compute, hardware=Hardware.objects.get(hardware="sensor-bme280-1"))

            # 3. resource-usbhub-10port
            # 4. resource-wagman
            # 5. resource-gps-1
            Resource.objects.create(node=n, hardware=Hardware.objects.get(hardware="resource-usbhub-10port"))
            Resource.objects.create(node=n, hardware=Hardware.objects.get(hardware="resource-wagman"))
            Resource.objects.create(node=n, hardware=Hardware.objects.get(hardware="resource-gps-1"))

            # 6. psu: psu-1 for nodes before (but not include) W040, psu-2 for nodes after W040
            # 7. wifi: for nodes after W040
            if row["flag"] == "group1":
                Resource.objects.create(node=n, hardware=Hardware.objects.get(hardware="resource-psu-1"))
            else:
                Resource.objects.create(node=n, hardware=Hardware.objects.get(hardware="resource-psu-2"))
                Resource.objects.create(node=n, hardware=Hardware.objects.get(hardware="resource-wifi-1"))


            # top_camera
            if row["top_camera"] != "none":
                if row["top_camera"].strip() == "True PTZ (XNP-6400RW)":
                    h_str = "sensor-camera-true-ptz-6400-1"
                elif row["top_camera"].strip() == "Thermal (mobotix)":
                    h_str = "sensor-camera-thermal-mobotix-1"
                else:
                    camera_type = row["top_camera"].split()[0].lower()
                    number = row["top_camera"].split("-")[1][:4]
                    h_str = "sensor-camera-" + camera_type + "-" + number + "-1"

                if not Hardware.objects.filter(hardware=h_str):
                    Hardware.objects.create(hardware=h_str)
                    print("Created a new hardware: " + h_str)
                h = Hardware.objects.get(hardware=h_str)
                NodeSensor.objects.create(node=n,hardware=h)

            # bottom_camera
            if row["bottom_camera"] != "none":
                if row["bottom_camera"].strip() == "True PTZ (XNP-6400RW)":
                    h_str = "sensor-camera-true-ptz-6400-1"
                elif row["bottom_camera"].strip() == "Thermal (mobotix)":
                    h_str = "sensor-camera-thermal-mobotix-1"
                else:
                    camera_type = row["bottom_camera"].split()[0].lower()
                    number = row["bottom_camera"].split("-")[1][:4]
                    h_str = "sensor-camera-" + camera_type + "-" + number + "-1"

                if not Hardware.objects.filter(hardware=h_str):
                    Hardware.objects.create(hardware=h_str)
                    print("Created a new hardware: " + h_str)
                h = Hardware.objects.get(hardware=h_str)
                NodeSensor.objects.create(node=n,hardware=h)

            # left_camera
            if row["left_camera"] != "none":
                if row["left_camera"].strip() == "True PTZ (XNP-6400RW)":
                    h_str = "sensor-camera-true-ptz-6400-1"
                elif row["left_camera"].strip() == "Thermal (mobotix)":
                    h_str = "sensor-camera-thermal-mobotix-1"
                else:
                    camera_type = row["left_camera"].split()[0].lower()
                    number = row["left_camera"].split("-")[1][:4]
                    h_str = "sensor-camera-" + camera_type + "-" + number + "-1"

                if not Hardware.objects.filter(hardware=h_str):
                    Hardware.objects.create(hardware=h_str)
                    print("Created a new hardware: " + h_str)
                h = Hardware.objects.get(hardware=h_str)
                NodeSensor.objects.create(node=n,hardware=h)

            # right_camera
            if row["right_camera"] != "none":
                if row["right_camera"].strip() == "True PTZ (XNP-6400RW)":
                    h_str = "sensor-camera-true-ptz-6400-1"
                elif row["right_camera"].strip() == "Thermal (mobotix)":
                    h_str = "sensor-camera-thermal-mobotix-1"
                else:
                    camera_type = row["right_camera"].split()[0].lower()
                    number = row["right_camera"].split("-")[1][:4]
                    h_str = "sensor-camera-" + camera_type + "-" + number + "-1"

                if not Hardware.objects.filter(hardware=h_str):
                    Hardware.objects.create(hardware=h_str)
                    print("Created a new hardware: " + h_str)
                h = Hardware.objects.get(hardware=h_str)
                NodeSensor.objects.create(node=n,hardware=h)

            # nx_agent
            if row["nx_agent"] == "yes":
                poe = Hardware.objects.get(hardware="compute-xaviernx-poe")
                n.computes.add(poe)
                Compute.objects.filter(node=n, hardware=poe).update(zone="agent")

            # shield
            if row["shield"] == "yes":
                if row["flag"] == "group1":
                    rpi4 = Hardware.objects.get(hardware="compute-rpi-4gb")
                    c1 = Compute.objects.create(node=n, hardware=rpi4)
                    Compute.objects.filter(node=n, hardware=rpi4).update(zone="shield")

                    ComputeSensor.objects.create(scope=c1, hardware=Hardware.objects.get(hardware="sensor-bme680-1"))
                    ComputeSensor.objects.create(scope=c1, hardware=Hardware.objects.get(hardware="sensor-microphone-1"))
                    ComputeSensor.objects.create(scope=c1, hardware=Hardware.objects.get(hardware="sensor-rainguage-1"))
                else:
                    rpi8 = Hardware.objects.get(hardware="compute-rpi-8gb")
                    c2 = Compute.objects.create(node=n, hardware=rpi8)
                    Compute.objects.filter(node=n, hardware=rpi8).update(zone="shield")

                    ComputeSensor.objects.create(scope=c2, hardware=Hardware.objects.get(hardware="sensor-bme680-1"))
                    ComputeSensor.objects.create(scope=c2, hardware=Hardware.objects.get(hardware="sensor-microphone-1"))
                    ComputeSensor.objects.create(scope=c2, hardware=Hardware.objects.get(hardware="sensor-rainguage-1"))


