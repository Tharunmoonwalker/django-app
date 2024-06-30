from django.shortcuts import redirect, render
from django.http import HttpResponse
from requests import session
from .models import product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import stripe
from .models import OrderDetail

# Create your views here.
def index(response):
    return HttpResponse("Hello People!")

def products(request):
    page_obj=products= product.objects.all()
    product_name=request.GET.get('product_name')
    if product_name!='' and product_name is not None:

        page_obj=products.filter(name__icontains=product_name)

    paginator=Paginator(page_obj,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'page_obj':page_obj
    }
    return render(request,'myapp/index.html',context)

#Class based view for listing products#

class ProductList(ListView):
    model=product
    template_name='myapp/index.html'
    context_object_name='products'
    paginate_by = 3
    


def product_detail(request,id):
    Product=product.objects.get(id=id)
    context={
        'product':Product
    }
    return render(request,'myapp/detail.html',context)

#class based view for  product details#
class ProductDetail(DetailView):
    model=product
    template_name='myapp/detail.html'
    context_object_name='product'
    pk_url_kwargs='pk'

    def get_context_data(self, **kwargs):
        context=super(ProductDetail,self).get_context_data(**kwargs)
        context['stripe_publishable_key']=settings.STRIPE_PUBLISHABLE_KEY
        return context

@login_required
def add_product(request): 
    if request.method=='POST':
        seller_name=request.user
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image=request.FILES.get('image')
        Products=product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
        Products.save()
        return redirect('/myapp/products')
    return render(request, 'myapp/addproduct.html')

#Class based view for adding products#
class AddProduct(CreateView):
    model=product
    fields=['name','price','desc','image','seller_name']
  #  product_form.html

def update_product(request,id):
    Product=product.objects.get(id=id)
    if request.method=='POST':
        Product.name=request.POST.get('name')
        Product.price=request.POST.get('price')
        Product.desc=request.POST.get('desc')
        Product.image=request.FILES.get('image')
        Product.save()
        return redirect('/myapp/products')
    context={
        'product':Product
    }
    return render(request, 'myapp/updateproduct.html', context)

def delete_product(request,id):
    Product=product.objects.get(id=id)
    if request.method=='POST':
        Product.delete()
        return redirect('/myapp/products')
    context={
        'product':Product
    }
    return render(request, 'myapp/deleteproduct.html', context)


def my_listings(request):
    products=product.objects.filter(seller_name=request.user) 
    context={
        'products':products
    }
    return render(request, 'myapp/mylistings.html', context)

@csrf_exempt
def create_checkout_session(request,id):
    Product=get_object_or_404(product,pk=id)
    stripe.api_key=settings.STRIPE_SECRET_KEY
    checkout_session=stripe.checkout.Session.create(
        customer_email=request.user.email,
        payment_method_types=['card'],
        line_items=[
            {
                'price_data':{
                    'currency':'usd',
                    'product_data':{
                        'name':Product.name,
                    },
                    'unit_amount':int(Product.price*100),
                },
                'quantity':1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('myapp:success'))+"?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('myapp:cancel')),

    )
    order=OrderDetail()
    order.customer_username=request.user.username
    order.product= Product
    order.stripe_payment_intent= checkout_session['id']
    order.amount=int(Product.price*100)
    order.save()
    return JsonResponse({'sessionId':checkout_session.id})

class PaymentSuccess(TemplateView):
    template_name='myapp/payment_success.html'

    def get(self, request, *args, **kwargs):
        session_id=request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()        
        session=stripe.checkout.Session.retrieve(session_id)
        stripe.api_key=settings.STRIPE_SECRET_KEY
        order = get_object_or_404(OrderDetail,stripe_payment_intent=session.id)
        order.has_paid=True
        order.save()
        return render(request,self.template_name)

class PaymentCancel(TemplateView):
    template_name='myapp/payment_cancel.html'