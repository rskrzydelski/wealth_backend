from rest_framework.serializers import ModelSerializer

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
