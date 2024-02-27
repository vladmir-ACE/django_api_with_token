
from pickle import NONE
from rest_framework import serializers
from .models import Users


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=("username", "role","password")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password=validated_data.get("password",NONE)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance

           
            


class UserLoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model=Users
        fields=("username","password")
    

