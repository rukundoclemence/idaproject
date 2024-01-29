from rest_framework import serializers
from .models import *

class userRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = student 
        fields = ['name', 'email', 'phone']