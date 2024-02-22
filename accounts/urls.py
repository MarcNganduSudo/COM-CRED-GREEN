from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/',views.register,name='register'),
    path('accounts/login/',views.login,name='login'),
    path('accounts/logout/',views.logout,name='logout'),
    path('accounts/dashboard/',views.dashboard,name='dashboard'),
    path('accounts/',views.dashboard,name='dashboard'),
    path('accounts/forgotPassword/',views.forgotPassword,name='forgotPassword'),
    path('accounts/activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('accounts/resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name='resetpassword_validate'),
    path('accounts/resetPassword/',views.resetPassword,name='resetPassword'),
    
    path('accounts/my_orders/',views.my_orders,name="my_orders"),
    path('accounts/edit_profile/',views.edit_profile,name="edit_profile"),
    path('accounts/change_password/',views.change_password,name="change_password"),
    path('accounts/order_detail/<int:order_id>/',views.order_detail,name="order_detail"),
    path('accounts/us/',views.us,name="us"),
]
