from dataclasses import field
from traceback import print_tb
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'leader')
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password','username','is_staff',)
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            password = validated_data['password'], 
            email=validated_data['email'], 
            is_staff=validated_data['is_staff']
            )
        return user


        
class UserDetailSerializer(serializers.ModelSerializer):
    leader = UserSerializer()
    class Meta:
        model = User
        fields = ('email', 'username','leader')
        
class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'is_active')
        
    def update(self, instance, validated_data):
        print(validated_data)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
class UserLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','leader')
        
    def update(self, instance, validated_data):
        
        instance.leader = validated_data.get('leader', instance.leader)
        instance.save()
        return instance
    
    