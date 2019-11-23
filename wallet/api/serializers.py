from rest_framework import serializers

from ..aggregators import MetalWalletData, CashWalletData, CurrencyWalletData, WalletData


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


class CashWalletSerializer(serializers.Serializer):
    my_currency = serializers.CharField(max_length=4)
    cash = serializers.DecimalField(max_digits=7, decimal_places=2)

    def create(self, validated_data):
        return CashWalletData(**validated_data)

    def update(self, instance, validated_data):
        instance.my_currency = validated_data.get('my_currency', instance.my_currency)
        instance.cash = validated_data.get('cash', instance.cash)


class CurrencyWalletSerializer(serializers.Serializer):
    total_value = serializers.DecimalField(max_digits=7, decimal_places=2)
    currency_name = serializers.CharField(max_length=4)

    def create(self, validated_data):
        return CurrencyWalletData(**validated_data)

    def update(self, instance, validated_data):
        instance.total_value = validated_data.get('total_value', instance.total_value)
        instance.currency_name = validated_data.get('currency_name', instance.currency_name)
        return instance


class WalletSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    my_fortune = serializers.DecimalField(max_digits=7, decimal_places=2)

    def create(self, validated_data):
        return WalletData(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.my_fortune = validated_data.get('my_fortune', instance.my_fortune)
        return instance
