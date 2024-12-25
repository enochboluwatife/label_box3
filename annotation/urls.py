from django.urls import path
from .views import home, AnnotationTaskView
from django.conf.urls.static import static
from django.urls import path
from . import views




from django.urls import path
from .views import home, view_annotations, AnnotationTaskView

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('view_annotations/', view_annotations, name='view_annotations'),  # View Annotations page
    path('api/tasks/', AnnotationTaskView.as_view(), name='annotation_tasks_api'),  # API endpoint
]
