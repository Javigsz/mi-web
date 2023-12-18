from django.contrib import admin

# Register your models here.
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    
    class Media:
        css = {
            'all': ('portfolio/css/custom_ckeditor.css',)
        }

admin.site.register(Project, ProjectAdmin)