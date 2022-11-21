from django.test import TestCase
from .models import *
import json

class HomepageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/ManifestApp/")
        self.assertEqual(response.status_code, 200)

class NodeTest(TestCase):
    def setUp(self):
        self.Node = NodeData.objects.create(VSN="A", name="A_name", gps_lat=50.00, gps_lan=50.00)

        tag1 = Tag.objects.create(tag="t1")
        self.Node.tags.set([tag1.pk])

        compute1 = Hardware.objects.create(hardware="h1")
        self.Node.computes.set([compute1.pk])

        self.response = self.client.get("/ManifestApp/api/nodes/")

    def test_node_creation(self):
        N = self.Node
        self.assertTrue(isinstance(N, NodeData))

    def test_node_has_a_tag(self):
        N = self.Node
        self.assertEqual(N.tags.count(), 1)

    def test_node_has_a_compute(self):
        N = self.Node
        self.assertEqual(N.computes.count(), 1)

    def test_contains_expected_fields(self):
        data = json.loads(self.response.content)

        self.assertEqual(data[0].keys(), set(['VSN', 'name', 'resources', 'sensors', 'gps_lat', 'gps_lan', 'tags', 'computes']))