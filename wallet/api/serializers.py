from rest_framework import serializers

from ..aggregators import MetalWalletData


class MetalWalletSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    my_currency = serializers.CharField(max_length=4)
    total_cash = serializers.DecimalField(max_digits=7, decimal_places=2)
    total_cash_spend = serializers.DecimalField(max_digits=7, decimal_places=2)
    profit = serializers.DecimalField(max_digits=7, decimal_places=2)

    def create(self, validated_data):
        return MetalWalletData(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.my_currency = validated_data.get('my_currency', instance.my_currency)
        instance.total_cash = validated_data.get('total_cash', instance.total_cash)
        instance.total_cash_spend = validated_data.get('total_cash_spend', instance.total_cash_spend)
        instance.profit = validated_data.get('profit', instance.profit)
        return instance

