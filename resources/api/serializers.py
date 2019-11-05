from rest_framework.serializers import ModelSerializer, SerializerMethodField

from resources.models import Metal


class MetalListSerializer(ModelSerializer):
    class Meta:
        model = Metal
        fields = [
            'id',
            'name',
            'amount',
            'unit',
            'date_of_bought'
        ]


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
            'id',
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