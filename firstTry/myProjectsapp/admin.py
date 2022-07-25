from django.contrib import admin

# Register your models here.
from .models import Project, Category


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'create_date']


admin.site.register(Category)
