from django.contrib import admin
from django.urls import path
from . import views
app_name='myapp'
urlpatterns = [
    path('hello/', views.index),
    path('products/',views.products, name="products"),
    path('products/<int:pk>/',views.ProductDetail.as_view(),name='product_detail'),
    path('products/add',views.add_product,name="add_product"),
    path('products/update/<int:id>', views.update_product, name='update_product'),
    path('products/delete/<int:id>', views.delete_product, name='delete_product'),
    path('products/mylistings/', views.my_listings, name="mylistings"),
    path('success/',views.PaymentSuccess.as_view(), name="success"),
    path('cancelled/',views.PaymentCancel.as_view(), name="cancel"),
    path('api/checkout-session/<id>', views.create_checkout_session, name='api_checkout_session'),
]   