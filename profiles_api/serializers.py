from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=15)
    lastName=serializers.CharField(max_length=20)
