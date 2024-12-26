from django.urls import path
from .views import home, AnnotationTaskView
from django.conf.urls.static import static
from django.urls import path
from . import views


from django.urls import path
from .views import AnnotationTaskView

urlpatterns = [
    path('tasks/', AnnotationTaskView.as_view(), name='annotation_tasks'),
]
