from django.contrib import admin

# Register your models here.
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    
    class Media:
        pass

admin.site.register(Link, LinkAdmin)