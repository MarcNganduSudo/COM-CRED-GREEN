import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from carts.models import CartItem
from .models import Order, Payment
from .forms import OrderForm
import json
from django.core.exceptions import ObjectDoesNotExist  # Importez ObjectDoesNotExist depuis django.core.exceptions

def payments(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        try:
            orders = Order.objects.filter(is_ordered=False)
            if orders.exists():
                for order in orders:
                    payment = Payment(
                        user=request.user,
                        payment_id=data['orderID'],
                        payment_method=data['payment_method'],
                        amount_paid=order.order_total,
                        status=data['status']
                    )
                    payment.save()
                    order.payment = payment
                    order.is_ordered = True
                    order.save()
                return JsonResponse(data)
            else:
                return JsonResponse({'error': 'Order not found'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Object does not exist'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def place_order(request,total=0, quantity=0):
    current_user=request.user
    cart_items=CartItem.objects.filter(user=current_user)
    cart_count=cart_items.count()
    if cart_count <= 0:
        return redirect('store')
    
    grand_total = 0
    tax=0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    
    tax=(2*total)/100
    grand_total = total+tax
    
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data=Order()
            data.user=current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total=grand_total
            data.tax=tax
            data.ip =request.META.get('REMOTE_ADDR')
            data.save()
            
            #generate order number
            yr=int(datetime.date.today().strftime('%Y'))
            dt=int(datetime.date.today().strftime('%d'))
            mt=int(datetime.date.today().strftime('%m'))
            d=datetime.date(yr,mt,dt)
            current_date=d.strftime("%Y%m%d")
            order_number=current_date+str(data.id)
            data.order_number=order_number
            data.save()
            order=Order.objects.get(user=current_user,is_ordered=False,order_number=order_number)
            
            context={
                'order':order,
                'cart_items':cart_items,
                'total':total,
                'tax':tax,
                'grand_total':grand_total
                
            }
            return render(request,'orders/payment.html',context)
            
        return redirect('checkout')
            
    else:
        return redirect('checkout')
    
    
def order_complete(request):
    return render(request,'orders/order_complete.html')
   
