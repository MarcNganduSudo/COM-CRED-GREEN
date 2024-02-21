from audioop import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
# nous allons configurer compte admin faire en sorte qu'on puisse tout modifier' 

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("User mast have an email address")
        if not username:
            raise ValueError("User mast have an username")
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
        
        
    def create_superuser(self,first_name,last_name,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user
        
class Accounts(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)
    
    
    date_join=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']
    
    objects=MyAccountManager()
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True
    
class UserProfile(models.Model):
    user=models.OneToOneField(Accounts,on_delete=models.CASCADE)
    address_line_1=models.CharField(max_length=100,blank=True,default=False)
    address_line_2=models.CharField(max_length=100,blank=True,default=False)
    profile_picture=models.ImageField(blank=True,upload_to='userprofile',default=False)
    city=models.CharField(max_length=20,blank=True,default=False)
    state=models.CharField(max_length=20,blank=True,default=False)
    country=models.CharField(max_length=20,blank=True,default=False)
    
    def __str__(self):
        return self.user.first_name
    
    def __str__(self):
        return f'{self.address_line_1}{self.address_line_2}' 
    

class Shop(models.Model):
    photo1 = models.ImageField(upload_to='photo/categories',blank=True)
    photo2 = models.ImageField(upload_to='photo/categories',blank=True)
    name = models.CharField(max_length=50, blank=True)
    sub_name = models.CharField(max_length=255, blank=True)
    description1 = models.TextField()
    description_block1_2 = models.TextField()
    description_block2_2 = models.TextField()
    description_block3 = models.TextField()
    description_block1_4 = models.TextField()
    description_block2_4 = models.TextField()
    def get_url(self):
        # dans reverse il y aura le name qu'on a utiliser pour faire la recherche de category dans store.urls'
        return reverse('shop_by_account',args=[self.slug])
        

    
