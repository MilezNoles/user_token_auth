from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAdminOrReadOnly
from api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)

