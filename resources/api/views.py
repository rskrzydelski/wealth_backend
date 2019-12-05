from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


from .serializers import (
    MetalListSerializer,
    MetalCreateSerializer,
    MetalDetailSerializer,
    CurrencyListSerializer,
    CurrencyCreateSerializer,
    CurrencyDetailSerializer,
    CashListSerializer,
    CashCreateSerializer,
)
from resources.models import Metal, Currency, Cash


class MetalLstCreateAPIView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MetalListSerializer
        else:
            return MetalCreateSerializer

    def get_queryset(self):
        # collect query strings
        query_name = self.request.GET.get('name')
        query_sum = self.request.GET.get('sum')

        if query_sum == 'true' and query_name:
            # make fake queryset with only one model with sum up data
            original_qs = Metal.objects.filter(owner=self.request.user, name=query_name)
            queryset = list()
            queryset.append(original_qs.first())
        else:
            queryset = Metal.objects.get_metal_list(owner=self.request.user, name=query_name)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if self.request.method == 'GET':
            if self.request.GET.get('sum') == 'true' and self.request.GET.get('name'):
                serializer = self.get_serializer_class()(queryset, many=True, fields=('name',
                                                                                      'unit',
                                                                                      'total_amount',
                                                                                      'total_cash_spend',))
            else:
                serializer = self.get_serializer_class()(queryset, many=True, fields=('name',
                                                                                      'amount',
                                                                                      'unit',
                                                                                      'bought_price',
                                                                                      'date_of_bought',))
        else:
            serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)


class MetalDetailDelUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MetalDetailSerializer

    def get_queryset(self):
        queryset = Metal.objects.filter(owner=self.request.user)
        return queryset


class CurrencyLstCreateAPIView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CurrencyListSerializer
        else:
            return CurrencyCreateSerializer

    def get_queryset(self):
        query_name = self.request.GET.get('name')
        query_sum = self.request.GET.get('sum')

        if query_sum == 'true' and query_name:
            # make fake queryset with only one model with sum up data
            original_qs = Currency.objects.get_currency_list(owner=self.request.user, currency=query_name)
            queryset = list()
            queryset.append(original_qs.first())
        else:
            queryset = Currency.objects.get_currency_list(owner=self.request.user, currency=query_name)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if self.request.method == 'GET':
            if self.request.GET.get('sum') == 'true' and self.request.GET.get('name'):
                serializer = self.get_serializer_class()(queryset, many=True, fields=('currency',
                                                                                      'total_currency',))
            else:
                serializer = self.get_serializer_class()(queryset, many=True, fields=('currency',
                                                                                      'bought_currency',
                                                                                      'bought_price',
                                                                                      'date_of_bought',))
        else:
            serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CurrencyDetailAPIView(RetrieveAPIView):
    serializer_class = CurrencyDetailSerializer

    def get_queryset(self):
        queryset = Currency.objects.filter(owner=self.request.user)
        return queryset


class CashLstCreateAPIView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CashListSerializer
        else:
            return CashCreateSerializer

    def get_queryset(self):
        query_sum = self.request.GET.get('sum')

        if query_sum == 'true':
            # make fake queryset with only one model with sum up data
            original_qs = Cash.objects.get_cash_list(owner=self.request.user)
            queryset = list()
            queryset.append(original_qs.first())
        elif query_sum:
            # incorrect query param
            queryset = Cash.objects.none()
        else:
            # without query param return list
            queryset = Cash.objects.get_cash_list(owner=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if self.request.method == 'GET':
            if self.request.GET.get('sum') == 'true':
                serializer = self.get_serializer_class()(queryset, many=True, fields=('my_currency',
                                                                                      'total_cash',))
            else:
                serializer = self.get_serializer_class()(queryset, many=True, fields=('my_currency',
                                                                                      'save_date',
                                                                                      'my_cash',))
        else:
            serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(my_cash_currency=self.request.user.my_currency)

