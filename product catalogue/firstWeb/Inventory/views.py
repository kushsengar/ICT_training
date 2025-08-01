from django.shortcuts import render , redirect
from Inventory.models import test

# Create your views here.
def home_inventory(request):
    data = test.objects.all() #getting all the data from the table to django
    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('price')
        var3 = request.POST.get('quantity')
        var4 = request.POST.get('discount')

        test_instance = test(name=var1 , price = var2 , quantity = var3 , discount = var4)
        test_instance.save()
        return redirect('home_inventory')
    return render(request , "home_inventory.html" , {"data":data,})

def edit(request , id):
    data = test.objects.get(id=id)
    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('quantity')
        var3 = request.POST.get('price')
        var4 = request.POST.get('discount')


        data.name = var1
        data.quantity = var2
        data.price = var3
        data.discount = var4
        data.save()
        return redirect('home_inventory')
    return render(request , 'edit_I.html' ,{'data':data ,})
   

def delete(request , id):
    data = test.objects.get(id=id)
    data.delete()
    return redirect('home_inventory')
