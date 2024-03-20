from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
import uuid



class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'email', 'password','confirm_password','mobile','address','role','is_active']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            # 'email': {'required': True},
            # 'password': {'write_only': True}
        }
        
    def validate(self, attr):
        if attr['password'] != attr['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attr
    
    def create(self, validated_data):
        unique_username = uuid.uuid4().hex 
        validated_data['username'] = unique_username
        validated_data.pop('confirm_password', None)
        user = User.objects.create(
            username=unique_username,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            address=validated_data['address'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
        
        # password = validated_data.pop('password', None)
        # instance = self.Meta.model(**validated_data)
        # if password is not None:
        #     instance.set_password(password)
        # instance.save()
        # return instance