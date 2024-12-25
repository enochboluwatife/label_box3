from rest_framework import serializers
from .models import AnnotationTask

class AnnotationTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotationTask
        fields = '__all__'
