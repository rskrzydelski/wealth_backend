import pytest
import json

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import RequestFactory, Client

from ..models import Metal


@pytest.fixture(params=[['Ag', '1000', 'PLN'],
                        ['Au', '6000', 'PLN'],
                        ['Ag', '250', 'USD'],
                        ['Au', '1500', 'USD']])
def metal_data(request):
    data = {
        'name': request.param[0],
        'bought_price_0': request.param[1],
        'bought_price_1': request.param[2],
        'date_of_bought': '2016-11-23 13:30:23',
        'amount': '10',
        'unit': 'oz',
    }
    return data


@pytest.fixture
def start_authentication(db):
    c = Client()
    User.objects.create_user(username='raf', password='abcd123abcd')
    c.login(username='raf', password='abcd123abcd')
    return c


@pytest.fixture
def create_metals(start_authentication, metal_data):
    url = reverse('resources:new-metal')
    res = start_authentication.post(url, metal_data)
    return res


def test_new_metal_status_ok(start_authentication):
    url = reverse('resources:new-metal')
    res = start_authentication.get(url)
    assert res.status_code == 200


def test_create_new_metal(create_metals):
    assert create_metals.status_code == 302
    assert Metal.objects.exists()


def test_delete_metal(start_authentication, create_metals):
    metal = Metal.objects.first()
    url = reverse('resources:del-metal', kwargs={'pk': metal.id})
    res = start_authentication.post(url)
    assert res.status_code == 302
    assert Metal.objects.exists() is False


@pytest.fixture
def basic_data():
    data = {
        'name': 'Au',
        'bought_price_0': '6500',
        'bought_price_1': 'PLN',
        'date_of_bought': '2016-11-23 13:30:23',
        'amount': '1',
        'unit': 'oz',
    }
    return data


@pytest.mark.parametrize('data_for_modify', [{
        'name': 'Ag',
        'bought_price_0': '2000',
        'bought_price_1': 'CHF',
        'date_of_bought': '2019-11-23 13:30:23',
        'amount': '2',
        'unit': 'oz',
    }])
def test_edit_metal(start_authentication, basic_data, data_for_modify):
    """test edit resource and status code as redirect"""
    url = reverse('resources:new-metal')
    start_authentication.post(url, basic_data)
    metal = Metal.objects.first()

    url = reverse('resources:edit-metal', kwargs={'pk': metal.id})
    res = start_authentication.post(url, data_for_modify)
    metal = Metal.objects.get(pk=metal.id)

    assert res.status_code == 302
    assert metal.name == data_for_modify['name']
    assert str(metal.bought_price.amount.to_integral()) == data_for_modify['bought_price_0']
    assert str(metal.bought_price.currency) == data_for_modify['bought_price_1']
    assert metal.date_of_bought.strftime("%Y-%m-%d %H:%M:%S") == data_for_modify['date_of_bought']
    assert str(metal.amount) == data_for_modify['amount']
    assert metal.unit == data_for_modify['unit']


def test_metal_list_status_ok(start_authentication):
    """test metal list"""
    # mixer.cycle(10).blend(Metal)
    url = reverse('resources:metal-list', kwargs={'slug': 'Ag'})
    res = start_authentication.get(url)
    assert res.status_code == 200

