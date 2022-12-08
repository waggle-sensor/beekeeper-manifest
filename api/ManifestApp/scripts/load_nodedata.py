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
            # 1. xaviernx
            nx = ComputeHardware.objects.get(hardware="xaviernx")
            n.computes.add(nx)
            Compute.objects.filter(node=n, hardware=nx).update(zone="core")
            Compute.objects.filter(node=n, hardware=nx).update(serial_no=row["node_id"][4:])

            # 2. bme280
            # 3. gps
            compute = Compute.objects.get(node=n, hardware=nx)
            ComputeSensor.objects.create(scope=compute, hardware=SensorHardware.objects.get(hardware="bme280"))
            NodeSensor.objects.create(node=n, hardware=SensorHardware.objects.get(hardware="gps"))

            # 4. usbhub-10port
            # 5. wagman
            Resource.objects.create(node=n, hardware=ResourceHardware.objects.get(hardware="usbhub-10port"))
            Resource.objects.create(node=n, hardware=ResourceHardware.objects.get(hardware="wagman"))

            # 6. psu: psu-B0BD for nodes before (but not include) W040, psu-BBBD for nodes after W040
            # 7. wifi: for nodes after W040
            if row["flag"] == "group1":
                Resource.objects.create(node=n, hardware=ResourceHardware.objects.get(hardware="psu-B0BD"))
            else:
                Resource.objects.create(node=n, hardware=ResourceHardware.objects.get(hardware="psu-BBBD"))
                Resource.objects.create(node=n, hardware=ResourceHardware.objects.get(hardware="wifi"))


            # top_camera
            if row["top_camera"] != "none":
                if row["top_camera"].strip() == "True PTZ (XNP-6400RW)":
                    h_str = "camera-true-ptz-6400"
                elif row["top_camera"].strip() == "Thermal (mobotix)":
                    h_str = "camera-thermal-mobotix"
                else:
                    camera_type = row["top_camera"].split()[0].lower()
                    number = row["top_camera"].split("-")[1][:4]
                    h_str = "camera-" + camera_type + "-" + number

                if not SensorHardware.objects.filter(hardware=h_str):
                    SensorHardware.objects.create(hardware=h_str)
                    print("Created a new sensor hardware: " + h_str)
                h = SensorHardware.objects.get(hardware=h_str)
                NodeSensor.objects.create(node=n,hardware=h)

            # bottom_camera
            if row["bottom_camera"] != "none":
                if row["bottom_camera"].strip() == "True PTZ (XNP-6400RW)":
                    h_str = "camera-true-ptz-6400"
                elif row["bottom_camera"].strip() == "Thermal (mobotix)":
                    h_str = "camera-thermal-mobotix"
                else:
                    camera_type = row["bottom_camera"].split()[0].lower()
                    number = row["bottom_camera"].split("-")[1][:4]
                    h_str = "camera-" + camera_type + "-" + number

                if not SensorHardware.objects.filter(hardware=h_str):
                    SensorHardware.objects.create(hardware=h_str)
                    print("Created a new sensor hardware: " + h_str)
                h = SensorHardware.objects.get(hardware=h_str)
                NodeSensor.objects.create(node=n,hardware=h)

            # left_camera
            if row["left_camera"] != "none":
                if row["left_camera"].strip() == "True PTZ (XNP-6400RW)":
                    h_str = "camera-true-ptz-6400"
                elif row["left_camera"].strip() == "Thermal (mobotix)":
                    h_str = "camera-thermal-mobotix"
                else:
                    camera_type = row["left_camera"].split()[0].lower()
                    number = row["left_camera"].split("-")[1][:4]
                    h_str = "camera-" + camera_type + "-" + number

                if not SensorHardware.objects.filter(hardware=h_str):
                    SensorHardware.objects.create(hardware=h_str)
                    print("Created a new hardware: " + h_str)
                h = SensorHardware.objects.get(hardware=h_str)
                NodeSensor.objects.create(node=n,hardware=h)

            # right_camera
            if row["right_camera"] != "none":
                if row["right_camera"].strip() == "True PTZ (XNP-6400RW)":
                    h_str = "camera-true-ptz-6400"
                elif row["right_camera"].strip() == "Thermal (mobotix)":
                    h_str = "camera-thermal-mobotix"
                else:
                    camera_type = row["right_camera"].split()[0].lower()
                    number = row["right_camera"].split("-")[1][:4]
                    h_str = "camera-" + camera_type + "-" + number

                if not SensorHardware.objects.filter(hardware=h_str):
                    SensorHardware.objects.create(hardware=h_str)
                    print("Created a new sensor hardware: " + h_str)
                h = SensorHardware.objects.get(hardware=h_str)
                NodeSensor.objects.create(node=n,hardware=h)

            # nx_agent
            if row["nx_agent"] == "yes":
                poe = ComputeHardware.objects.get(hardware="xaviernx-poe")
                n.computes.add(poe)
                Compute.objects.filter(node=n, hardware=poe).update(zone="agent")

            # shield
            if row["shield"] == "yes":
                if row["flag"] == "group1":
                    rpi4 = ComputeHardware.objects.get(hardware="rpi-4gb")
                    c1 = Compute.objects.create(node=n, hardware=rpi4)
                    Compute.objects.filter(node=n, hardware=rpi4).update(zone="shield")

                    ComputeSensor.objects.create(scope=c1, hardware=SensorHardware.objects.get(hardware="bme680"))
                    ComputeSensor.objects.create(scope=c1, hardware=SensorHardware.objects.get(hardware="microphone"))
                    ComputeSensor.objects.create(scope=c1, hardware=SensorHardware.objects.get(hardware="rainguage"))
                else:
                    rpi8 = ComputeHardware.objects.get(hardware="rpi-8gb")
                    c2 = Compute.objects.create(node=n, hardware=rpi8)
                    Compute.objects.filter(node=n, hardware=rpi8).update(zone="shield")

                    ComputeSensor.objects.create(scope=c2, hardware=SensorHardware.objects.get(hardware="bme680"))
                    ComputeSensor.objects.create(scope=c2, hardware=SensorHardware.objects.get(hardware="microphone"))
                    ComputeSensor.objects.create(scope=c2, hardware=SensorHardware.objects.get(hardware="rainguage"))


