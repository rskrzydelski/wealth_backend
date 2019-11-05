from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .serializers import MetalListSerializer, MetalCreateSerializer, MetalDetailSerializer
from resources.models import Metal


class MetalLstCreateAPIView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MetalListSerializer
        else:
            return MetalCreateSerializer

    def get_queryset(self):
        query_name = self.request.GET.get('name')
        queryset = Metal.objects.get_metal_list(owner=self.request.user, name=query_name)
        return queryset


class MetalDetailAPIView(RetrieveAPIView):
    serializer_class = MetalDetailSerializer

    def get_queryset(self):
        queryset = Metal.objects.filter(owner=self.request.user)
        return queryset
