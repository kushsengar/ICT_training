from django.urls import path
from E_commerce_App.views import buyer_home ,signup , home , login_view ,view_cart, add_to_cart ,checkout, dashboard , seller_home,add_product,edit_product,delete_product ,custom_logout_view , otp_login_request ,verify_otp,user_profile,payment_success

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('seller/', seller_home, name='seller_home'),
    path('buyer/', buyer_home, name='buyer_home'),
    path('seller/add/', add_product, name='add_product'),
    path('seller/edit/<int:pk>/', edit_product, name='edit_product'),
    path('seller/delete/<int:pk>/', delete_product, name='delete_product'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
    path('logout/', custom_logout_view, name='logout'),
    path('otp-login/', otp_login_request, name='otp_login'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('profile/', user_profile, name='user_profile'), # Forgot Password
    path('payment-success/', payment_success, name='payment_success'),
]