from api.serializers import UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import authentication_classes, permission_classes
from api.models import User

@authentication_classes([]) # Add this
@permission_classes([]) # Maybe add this too
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]