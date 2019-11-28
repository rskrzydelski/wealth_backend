import json

from django.test import TestCase, override_settings

from resources.models import Currency
from accounts.models import InvestorUser


class CurrencyModelTestCase(TestCase):
    @override_settings(USE_TZ=False)
    def setUp(self):
        with open("./resources/tests/cfg/test_currency_data.config", "r") as currency_cfg:
            test_data = currency_cfg.read()

        self.investor_test = InvestorUser.objects.create_user(username='testuser', password='abc123')
        self.currency_test_data = json.loads(test_data)

        self.usd_test_data_1 = self.currency_test_data.get('usd_record_1')
        self.usd_test_data_2 = self.currency_test_data.get('usd_record_2')

        self.eur_test_data_1 = self.currency_test_data.get('eur_record_1')
        self.eur_test_data_2 = self.currency_test_data.get('eur_record_2')

        self.chf_test_data_1 = self.currency_test_data.get('chf_record_1')
        self.chf_test_data_2 = self.currency_test_data.get('chf_record_2')

        self.usd_test_obj_1 = Currency.objects.create(owner=self.investor_test, **self.usd_test_data_1)
        self.usd_test_obj_2 = Currency.objects.create(owner=self.investor_test, **self.usd_test_data_2)

        self.eur_test_obj_1 = Currency.objects.create(owner=self.investor_test, **self.eur_test_data_1)
        self.eur_test_obj_2 = Currency.objects.create(owner=self.investor_test, **self.eur_test_data_2)

        self.chf_test_obj_1 = Currency.objects.create(owner=self.investor_test, **self.chf_test_data_1)
        self.chf_test_obj_2 = Currency.objects.create(owner=self.investor_test, **self.chf_test_data_2)

    def test_currency_usd_check_fields(self):
        self.assertEqual(str(self.usd_test_obj_1.bought_price.amount), self.usd_test_data_1.get('bought_price'))
        self.assertEqual(self.usd_test_obj_1.bought_price_currency, self.usd_test_data_1.get('bought_price_currency'))
        self.assertEqual(self.usd_test_obj_1.date_of_bought, self.usd_test_data_1.get('date_of_bought'))
        self.assertEqual(str(self.usd_test_obj_1.bought_currency.amount), self.usd_test_data_1.get('bought_currency'))
        self.assertEqual(self.usd_test_obj_1.bought_currency_currency, self.usd_test_data_1.get('bought_currency_currency'))

    def test_currency_eur_check_fields(self):
        self.assertEqual(str(self.eur_test_obj_1.bought_price.amount), self.eur_test_data_1.get('bought_price'))
        self.assertEqual(self.eur_test_obj_1.bought_price_currency, self.eur_test_data_1.get('bought_price_currency'))
        self.assertEqual(self.eur_test_obj_1.date_of_bought, self.eur_test_data_1.get('date_of_bought'))
        self.assertEqual(str(self.eur_test_obj_1.bought_currency.amount), self.eur_test_data_1.get('bought_currency'))
        self.assertEqual(self.eur_test_obj_1.bought_currency_currency, self.eur_test_data_1.get('bought_currency_currency'))

    def test_currency_chf_check_fields(self):
        self.assertEqual(str(self.chf_test_obj_1.bought_price.amount), self.chf_test_data_1.get('bought_price'))
        self.assertEqual(self.chf_test_obj_1.bought_price_currency, self.chf_test_data_1.get('bought_price_currency'))
        self.assertEqual(self.chf_test_obj_1.date_of_bought, self.chf_test_data_1.get('date_of_bought'))
        self.assertEqual(str(self.chf_test_obj_1.bought_currency.amount), self.chf_test_data_1.get('bought_currency'))
        self.assertEqual(self.chf_test_obj_1.bought_currency_currency, self.chf_test_data_1.get('bought_currency_currency'))

