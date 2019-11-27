import json

from django.test import TestCase, override_settings

from resources.models import Metal
from accounts.models import InvestorUser


class MetalModelTestCase(TestCase):
    @override_settings(USE_TZ=False)
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

    def test_metal_silver_check_fields(self):
        self.assertEqual(self.silver_test_obj_1.name, self.silver_test_data_1.get('name'))
        self.assertEqual(str(self.silver_test_obj_1.bought_price.amount), self.silver_test_data_1.get('bought_price'))
        self.assertEqual(self.silver_test_obj_1.date_of_bought, self.silver_test_data_1.get('date_of_bought'))
        self.assertEqual(self.silver_test_obj_1.unit, self.silver_test_data_1.get('unit'))
        self.assertEqual(self.silver_test_obj_1.amount, self.silver_test_data_1.get('amount'))
        self.assertEqual(self.silver_test_obj_1.description, self.silver_test_data_1.get('description'))

    def test_metal_gold_check_fields(self):
        self.assertEqual(self.gold_test_obj_1.name, self.gold_test_data_1.get('name'))
        self.assertEqual(str(self.gold_test_obj_1.bought_price.amount), self.gold_test_data_1.get('bought_price'))
        self.assertEqual(self.gold_test_obj_1.date_of_bought, self.gold_test_data_1.get('date_of_bought'))
        self.assertEqual(self.gold_test_obj_1.unit, self.gold_test_data_1.get('unit'))
        self.assertEqual(self.gold_test_obj_1.amount, self.gold_test_data_1.get('amount'))
        self.assertEqual(self.gold_test_obj_1.description, self.gold_test_data_1.get('description'))
