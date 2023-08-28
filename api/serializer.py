from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ["id", "password","usarname"]
      

class ResgisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializer.Charfield(write_only=True, required= True)
    class Meta:
        model = User
        fields = ("username", 'password', 'password2',
                  )
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "password incorrecto por favor vuelva a ingresar"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username= validated_data['username'],
            password= validate_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user