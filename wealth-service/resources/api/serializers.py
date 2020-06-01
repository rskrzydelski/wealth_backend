from rest_framework.serializers import ModelSerializer, SerializerMethodField
from resources.models import Metal, Currency, Cash


class MetalListSerializer(ModelSerializer):
    class Meta:
        model = Metal
        fields = [
            'name',
            'amount',
            'unit',
            'bought_price',
            'bought_price_currency',
            'date_of_bought',
        ]


class MetalCreateSerializer(ModelSerializer):
    class Meta:
        model = Metal
        fields = [
            'name',
            'bought_price',
            'bought_price_currency',
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
            'bought_price_currency',
            'amount',
            'unit',
            'date_of_bought',
            'description',
        ]

    def get_bought_price(self, obj):
        return str(obj.bought_price)


class CurrencyListSerializer(ModelSerializer):
    currency = SerializerMethodField('get_currency')

    class Meta:
        model = Currency
        fields = [
            'owner',
            'currency',
            'bought_currency',
            'bought_price',
            'date_of_bought',
        ]

    def get_currency(self, obj):
        return str(obj.bought_currency_currency)


class CurrencyCreateSerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'bought_currency',
            'bought_currency_currency',
            'bought_price',
            'bought_price_currency',
            'date_of_bought',
        ]

    def validate(self, data):
        # if data['bought_currency'].currency == data['bought_price'].currency:
        #     raise serializers.ValidationError("Bought currency and currency which you pay can't be the same !")
        #
        # if str(data['bought_currency'].currency) == self.context['request'].user.my_currency:
        #     raise serializers.ValidationError("You can't buy your own currency !")
        print(data)
        return data


class CurrencyDetailSerializer(ModelSerializer):
    currency = SerializerMethodField('get_currency')

    class Meta:
        model = Currency
        fields = [
            'currency',
            'bought_currency',
            'bought_price',
            'date_of_bought',
        ]

    def get_currency(self, obj):
        return str(obj.bought_currency_currency)


class CashListSerializer(ModelSerializer):
    my_currency = SerializerMethodField('get_my_currency')

    class Meta:
        model = Cash
        fields = [
            'my_currency',
            'save_date',
            'my_cash',
        ]

    def get_my_currency(self, obj):
        return str(obj.owner.my_currency)


class CashCreateSerializer(ModelSerializer):
    class Meta:
        model = Cash
        fields = [
            'save_date',
            'my_cash',
        ]


class CashDetailSerializer(ModelSerializer):
    class Meta:
        model = Cash
        fields = [
            'owner',
            'save_date',
            'my_cash',
        ]
