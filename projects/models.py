from django.db import models
from ckeditor.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=200,default="domyślny tytuł")
    description = models.TextField(default="domyślny tekst")
    content = RichTextField(default="domyślny tekst")
    image = models.FileField(upload_to="project_images/", blank=True)
    
    def __str__(self):
        return self.title

