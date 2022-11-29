from ..models import *
import csv


def run():
    with open('ManifestApp/data/nodedata.csv') as file:
        reader = csv.DictReader(file)

        NodeData.objects.all().delete()

        for row in reader:
            print(row)

            node = NodeData.objects.create(vsn=row["vsn"].strip(),
                        gps_lat=float(row["gps_lat"].strip() or 0),
                        gps_lon=float(row["gps_lon"].strip() or 0),
                        )

            # Create Tag object only if nodedata.csv/tags column has value and the val does not exist in current Tag model
            if len(row["tags"].strip()) > 0:
                for t in row["tags"].split(","):
                    if not Tag.objects.filter(tag=t):
                        Tag.objects.create(tag=t)
                    tag = Tag.objects.get(tag=t)
                    node.tags.add(tag)

            if len(row["computes"].strip()) > 0:
                for c in row["computes"].split(","):
                    if not Hardware.objects.get(hardware=c):
                        print("Compute: " + c + "does not exist in hardware table")
                    compute = Hardware.objects.get(hardware=c)
                    node.computes.add(compute)

            if len(row["resources"].strip()) > 0:
                for r in row["resources"].split(","):
                    if not Hardware.objects.get(hardware=r):
                        print("Resource: " + r + "does not exist in hardware table")
                    resource = Hardware.objects.get(hardware=r)
                    node.computes.add(resource)




