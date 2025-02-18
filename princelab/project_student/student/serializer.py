from rest_framework import serializers
from .models import Student  # Assuming you have a Student model

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'