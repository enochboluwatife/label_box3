from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import AnnotationTask
from .serializers import AnnotationTaskSerializer

# Render the home page
def home(request):
    """
    Render the homepage where users can upload and annotate images.
    """
    return render(request, 'index.html')


# View to display saved annotations
def view_annotations(request):
    """
    Fetch and display all saved annotations with their corresponding images.
    """
    tasks = AnnotationTask.objects.all().order_by('-id')  # Fetch and order tasks by latest
    return render(request, 'view_annotations.html', {'tasks': tasks})


# API view for handling tasks
class AnnotationTaskView(APIView):
    """
    Handles CRUD operations for Annotation Tasks.
    """
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        """
        Retrieve and return all saved annotation tasks.
        """
        tasks = AnnotationTask.objects.all()
        serializer = AnnotationTaskSerializer(tasks, many=True)
        return Response({
            "status": "success",
            "message": "Annotations retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Save a new annotation task with the uploaded image and annotation text.
        """
        serializer = AnnotationTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Annotation saved successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "message": "Failed to save annotation.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
