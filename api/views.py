from rest_framework import permissions, viewsets
from django.contrib.auth import get_user_model
from . import serializers

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
