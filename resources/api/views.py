from rest_framework.generics import ListCreateAPIView

from .serializers import MetalListSerializer, MetalCreateSerializer
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
