from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import AnnotationTask
from .serializers import AnnotationTaskSerializer

# Render the home page
def home(request):
    return render(request, 'index.html')

# View to display saved annotations
def view_annotations(request):
    tasks = AnnotationTask.objects.all()  # Fetch all annotation tasks
    return render(request, 'view_annotations.html', {'tasks': tasks})


# API view for handling tasks
class AnnotationTaskView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        tasks = AnnotationTask.objects.all()
        serializer = AnnotationTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnnotationTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from .models import AnnotationTask
