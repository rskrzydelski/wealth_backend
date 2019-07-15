from django.db import models
from djmoney.models.fields import MoneyField


# data model common for all resources
class Resource(models.Model):
    current_price = MoneyField(max_digits=10, decimal_places=2, null=True, default=0, default_currency='PLN')
    bought_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='PLN')
    date_of_bought = models.DateTimeField(auto_now_add=False)
    amount = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    class Meta:
        abstract = True


# data model common for all metals
class Metal(Resource):
    METAL_CHOICES = [
        ('Ag', 'Silver'),
        ('Au', 'Gold'),
        ('Pd', 'Palladium'),
        ('Pt', 'Platinum'),
    ]
    UNIT_CHOICES = [
        ('oz', 'ounce'),
        ('g', 'gram'),
        ('kg', 'kilogram'),
    ]
    name = models.CharField(
        max_length=10,
        choices=METAL_CHOICES,
        default='Ag',
    )
    unit = models.CharField(max_length=10,
                            choices=UNIT_CHOICES,
                            default='oz')

    def __str__(self):
        return self.get_name_display()


# class Cash(models.Model):
#     CURRENCY_CHOICES = [('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ')]
#     currency = models.CharField(
#         max_length=10,
#         choices=CURRENCY_CHOICES,
#         default='PLN',
#     )


# class Land(Resource):
#     LAND_CHOICES = [
#         ('f', 'farmland'),
#         ('b', 'building'),
#     ]
#     AREA_TYPE = [
#         ('h', 'hectare'),
#     ]
#     type = models.CharField(
#         max_length=10,
#         choices=LAND_CHOICES,
#         default='b',
#     )
#     area_unit = models.CharField(max_length=10,
#                                  choices=AREA_TYPE,
#                                  default='h')


# class Wallet(models.Model):
#     models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     metal = models.ManyToManyField(Metal)
#     cash = models.ManyToManyField(Cash)
#
