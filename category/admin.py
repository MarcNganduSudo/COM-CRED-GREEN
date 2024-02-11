from django.contrib import admin
from .models import category

# Register your models here.
#faite que lorsque j'apuis sur categoriesque ca puisse allez directement dans slug

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name','slug')#queca puisse s'afficher en tableau
    
admin.site.register(category,CategoryAdmin)
