from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Project(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=500)
    path = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
