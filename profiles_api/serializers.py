from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    #here we define in the serializer what fields to be validated
    name = serializers.CharField(max_length=10)