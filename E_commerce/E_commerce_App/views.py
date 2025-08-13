from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from E_commerce_App.models import UserProfile , Product 
from E_commerce_App.forms import ProductForm,MobileForm, OTPForm
from E_commerce_App.utils import send_otp_sms
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required   
import random
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            # Step 1: Create User
            user = User.objects.create_user(username=username, email=email, password=password)

            # Step 2: Create related UserProfile
            UserProfile.objects.create(user=user, phone=phone, address=address)

            messages.success(request, "Account created successfully!")
            return redirect('signup')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('user_profile')  # Or wherever you want to take them
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

@login_required
# E_commerce_App/views.py

def seller_home(request):
    products = Product.objects.all()
    return render(request, 'seller_home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller_home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('seller_home')
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('seller_home')
    return render(request, 'confirm_delete.html', {'product': product})


@login_required
def buyer_home(request):
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    products = Product.objects.all()

    if category:
        products = products.filter(category=category)

    if sort == 'price_asc':
        products = products.order_by('discounted_price')
    elif sort == 'price_desc':
        products = products.order_by('-discounted_price')

    paginator = Paginator(products, 6)  # 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'buyer_home.html', {
        'products': page_obj,
        'category': category,
        'sort': sort
    })

from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Cart , Order

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

from .models import Cart

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

def checkout(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount")) * 100  # Amount in paise
        currency = 'INR'
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment_order = client.order.create(dict(amount=amount, currency=currency, payment_capture=1))
        payment_order_id = payment_order['id']
        context = {
            'amount': amount,
            'api_key': settings.RAZORPAY_KEY_ID,
            'order_id': payment_order_id,
        }
        return render(request, 'payment.html', context)
    return render(request, 'checkout.html')


def custom_logout_view(request):
    logout(request)
    return redirect('login')  # or redirect to home

OTP_STORAGE = {}

def otp_login_request(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            try:
                profile = UserProfile.objects.get(phone=phone)
                otp = str(random.randint(100000, 999999))
                OTP_STORAGE[phone] = otp

                # ✅ Send OTP via Fast2SMS
                response = send_otp_sms(phone, otp)
                print("Fast2SMS Response:", response)  # for debug/logging

                return render(request, 'enter_otp.html', {
                    'phone': phone,
                    'otp' : otp
                })

            except UserProfile.DoesNotExist:
                messages.error(request, "You are not registered with us.")
                return render(request, 'otp_login.html', {
                    'form': form,
                    'not_registered': True
                })
    else:
        form = MobileForm()
    return render(request, 'otp_login.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        phone = request.POST.get('phone')
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            actual_otp = OTP_STORAGE.get(phone)

            if actual_otp == entered_otp:
                try:
                    user_profile = UserProfile.objects.get(phone=phone)
                    login(request, user_profile.user)
                    messages.success(request, "Login successful via OTP!")
                    return redirect('user_profile')
                except UserProfile.DoesNotExist:
                    messages.error(request, "User not found.")
            else:
                messages.error(request, "Invalid OTP. Please try again.")

        return render(request, 'enter_otp.html', {
            'form': form,
            'phone': phone
        })
        
def user_profile(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None  # fallback, not expected in your app

    return render(request, 'user_profile.html', {
        'user': user,
        'profile': profile,
    })
    
    # views.py
from django.conf import settings
from django.shortcuts import render
import razorpay

# def payment_page(request):
#     if request.method == "POST":
#         amount = int(request.POST.get("amount")) * 100  # Amount in paise
#         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         payment = client.order.create({
#             "amount": amount,
#             "currency": "INR",
#             "payment_capture": 1
#         })
#         return render(request, "payment.html", {
#             "payment": payment,
#             "key_id": settings.RAZORPAY_KEY_ID
#         })
#     return render(request, "payment.html")

def payment_success(request):
    return render(request, 'payment_success.html')
