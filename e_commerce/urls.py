from django.contrib import admin
from django.urls import include, path
from e_commerce import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('',include('store.urls')) ,#cava me conduirevert un urls qui va a son tour me conduire vers views
    path('',include('carts.urls')) ,
    path('',include('accounts.urls')),
    
    #orders
    path('',include('orders.urls')),
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)







