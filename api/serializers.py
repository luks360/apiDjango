from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class PendingRequestSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = UserSerializer

    def to_representation(self):
        return UserSerializer().data