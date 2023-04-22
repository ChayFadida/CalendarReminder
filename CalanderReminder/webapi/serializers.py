from rest_framework import serializers
from Notify.models import UsersFriends

class UsersFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersFriends
        fields = '__all__' 