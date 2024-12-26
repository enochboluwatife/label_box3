from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AnnotationTask

class AnnotationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'annotated_text', 'created_at')  # Updated field names
    readonly_fields = ('image_preview',)  # To display image preview in the admin panel

    # Method to display image preview
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px;" />'
        return "No Image"
    image_preview.short_description = "Image Preview"
    image_preview.allow_tags = True

# Register the model with the custom admin class
admin.site.register(AnnotationTask, AnnotationTaskAdmin)
