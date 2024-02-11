from django.urls import reverse
from django.db import models

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    # nous voulons que dans le champ categorys lorsque je met une category automatiquement qu'il puisse se dupliquer dans slug et apres nous devons allez le sigmaler damns admin prepopulated_fields tutoriel'
    slug=models.SlugField(max_length=50,unique=True)
    description=models.TextField(max_length=255,blank=True)
    cat_image=models.ImageField(upload_to='photo/categories',blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
        # dans reverse il y aura le name qu'on a utiliser pour faire la recherche de category dans store.urls'
        return reverse('products_by_category',args=[self.slug])
    
    def __str__(self):
        return self.category_name
    

    
    
