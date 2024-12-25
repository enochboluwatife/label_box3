from django.urls import path
from .views import home, AnnotationTaskView
from django.conf.urls.static import static
from django.urls import path
from . import views





urlpatterns = [
    path('', home, name='home'),  # Home page
    path('tasks/', AnnotationTaskView.as_view(), name='annotation_tasks'),  # API for task
    path('view-annotations/', views.view_annotations, name='view_annotations'),
]
