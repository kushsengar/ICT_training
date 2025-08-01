from django.shortcuts import render, redirect
from  billmanagement.models import Customer, Order
from Inventory.models import test

def customer_create(request):
    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('mobile')
        var3 = request.POST.get('email')
        var4 = request.POST.get('address')
        
        create_instance = Customer(name = var1 , mobile = var2 , email = var3 , address = var4)
        create_instance.save()
        return redirect('order_create')
    return render(request, 'customer_create.html')

def order_create(request):
    customers = Customer.objects.all()
    products = test.objects.all()

    if request.method == 'POST':
        customer_id = request.POST['customer']
        product_id = request.POST['product']
        quantity = request.POST['quantity']

        Order.objects.create(
            customer_id=customer_id,
            product_id=product_id,
            quantity=quantity
        )
        return redirect('home_inventory')

    return render(request, 'order_create.html', {'customers': customers, 'products': products})
