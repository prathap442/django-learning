from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    #here we define in the serializer what fields to be validated
    name = serializers.CharField(max_length=10)


'''
    Why use Meta class?
    To point out the serializer to a specific models our project
    by name attribute in the Meta class serializer
'''
class UserProfileSerializer(serializers.ModelSerializer):
    """serializer for a userprofile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }  
            }
        }


    def create(self,validated_data):
        """creates and returns a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self,instance,validated_data):
        """updates the user stuff"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)            
        
        return super().update(instance, validated_data)
