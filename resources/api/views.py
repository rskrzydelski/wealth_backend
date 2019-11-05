from rest_framework.generics import ListCreateAPIView

from .serializers import MetalListSerializer
from resources.models import Metal


class MetalLstCreateAPIView(ListCreateAPIView):
    serializer_class = MetalListSerializer

    def get_queryset(self):
        query_name = self.request.GET.get('name')
        queryset = Metal.objects.get_metal_list(owner=self.request.user, name=query_name)
        return queryset
