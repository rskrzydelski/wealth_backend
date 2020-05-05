from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import UserSerializer

InvestorUser = get_user_model()


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = InvestorUser.objects.all()
    serializer_class = UserSerializer
