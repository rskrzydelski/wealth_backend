from rest_framework.serializers import ModelSerializer, SerializerMethodField

from resources.models import Metal, Currency


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MetalListSerializer(DynamicFieldsModelSerializer):
    total_amount = SerializerMethodField('get_total_amount')
    total_cash_spend = SerializerMethodField('get_total_cash_spend')

    class Meta:
        model = Metal
        fields = [
            'name',
            'amount',
            'unit',
            'bought_price',
            'date_of_bought',
            'total_amount',
            'total_cash_spend',
        ]

    def get_total_amount(self, obj):
        return str(Metal.objects.get_total_metal_amount(owner=obj.owner, name=obj.name))

    def get_total_cash_spend(self, obj):
        return str(Metal.objects.get_total_metal_cash_spend(owner=obj.owner, name=obj.name))


class MetalCreateSerializer(ModelSerializer):
    class Meta:
        model = Metal
        fields = [
            'name',
            'bought_price',
            'amount',
            'unit',
            'date_of_bought',
            'description',
        ]


class MetalDetailSerializer(ModelSerializer):
    bought_price = SerializerMethodField('get_bought_price')

    class Meta:
        model = Metal
        fields = [
            'owner',
            'name',
            'bought_price',
            'amount',
            'unit',
            'date_of_bought',
            'description',
        ]

    def get_bought_price(self, obj):
        return str(obj.bought_price)


class CurrencyListSerializer(DynamicFieldsModelSerializer):
    currency = SerializerMethodField('get_currency')
    total_currency = SerializerMethodField('get_total_currency')

    class Meta:
        model = Currency
        fields = [
            'owner',
            'currency',
            'bought_currency',
            'bought_price',
            'total_currency',
            'date_of_bought',
        ]

    def get_currency(self, obj):
        return str(obj.bought_currency_currency)

    def get_total_currency(self, obj):
        return str(Currency.objects.get_total_currency(owner=obj.owner, currency=obj.bought_currency_currency))
