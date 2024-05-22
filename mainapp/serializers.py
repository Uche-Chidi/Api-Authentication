from rest_framework import serializers, exceptions
from .models import Student



class StudentSerializer(serializers.Serializer):
    names=serializers.CharField(max_length=200)
    email=serializers.EmailField(max_length=70)
    age=serializers.IntegerField()
    address=serializers.CharField(max_length=200)


    def validate(self, attrs):
        age = attrs.get('age')
        if age < 18:
            raise exceptions.ValidationError("Age must be greater than 18")
        return attrs
    
    def create(self, validated_data):
        return validated_data
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

class StudentCreateSerializer(serializers.ModelSerializer):
    course=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Student
        fields=['id', 'names', 'age', 'email', 'address', 'course']
        
    
    def validate(self, attrs):
        age = attrs.get('age')
        if age < 18:
            raise exceptions.ValidationError("Age must be greater than 18")
        return attrs
class StudentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id', 'names', 'email']

