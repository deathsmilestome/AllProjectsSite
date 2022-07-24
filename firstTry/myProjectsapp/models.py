from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=500)
    lang = models.CharField(max_length=50)
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='project_imgs/', null = True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
