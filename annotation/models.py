from djongo import models

class AnnotationTask(models.Model):
    id = models.ObjectIdField(primary_key=True)
    image = models.ImageField(upload_to='uploads/')  # Save images to 'uploads/' directory
    annotated_text = models.TextField(blank=True, null=True)  # Text annotations
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task {self.id}"
