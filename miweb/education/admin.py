from django.contrib import admin

# Register your models here.
from .models import Language, Course

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    
    class Media:
        pass

class CourseAdmin(admin.ModelAdmin):
    
    class Media:
        pass

admin.site.register(Language, LanguageAdmin)
admin.site.register(Course, CourseAdmin)