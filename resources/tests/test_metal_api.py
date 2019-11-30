import json

from django.test import TestCase

from rest_framework.test import RequestsClient

from accounts.models import InvestorUser
from resources.models import Metal


class MetalApiTestCase(TestCase):
    def setUp(self):
        with open("./resources/tests/cfg/test_metal_data.config", "r") as metal_cfg:
            test_data = metal_cfg.read()

        self.investor_test = InvestorUser.objects.create_user(username='testuser', password='abc123')
        self.metal_test_data = json.loads(test_data)

        self.silver_test_data_1 = self.metal_test_data.get('silver_record_1')
        self.silver_test_data_2 = self.metal_test_data.get('silver_record_2')
        self.gold_test_data_1 = self.metal_test_data.get('gold_record_1')
        self.gold_test_data_2 = self.metal_test_data.get('gold_record_2')

        self.silver_test_obj_1 = Metal.objects.create(owner=self.investor_test, **self.silver_test_data_1)
        self.silver_test_obj_2 = Metal.objects.create(owner=self.investor_test, **self.silver_test_data_2)
        self.gold_test_obj_1 = Metal.objects.create(owner=self.investor_test, **self.gold_test_data_1)
        self.gold_test_obj_2 = Metal.objects.create(owner=self.investor_test, **self.gold_test_data_2)

        self.client = RequestsClient()
        response = self.client.post('http://127.0.0.1:8000/api/v1/auth/token', json={'username': 'testuser',
                                                                                'password': 'abc123'})
        content = json.loads(response.content)
        self.token = content.get('token')

