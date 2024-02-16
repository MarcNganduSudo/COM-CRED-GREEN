from django.urls import path
from . import views

urlpatterns = [
    path('orders/place_order/',views.place_order,name="place_order"),
    path('orders/payments/',views.payments,name="payments"),
    path('orders/place_order/orders/payments',views.payments,name="payments"),
    path('orders/order_complete/',views.order_complete,name="order_complete"),
]