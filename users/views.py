from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            User=form.save()
            return redirect('myapp/products')
    form=SignUpForm()
    context={
        'form':form
    }
    return render(request,"users/register.html", context)
@login_required
def profile(request):
    return render(request, 'users/profile.html')

def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES.get('image')
        user=request.user
        profile=Profile(user=user, contact_number=contact_number, image=image)
        profile.save()
    return render(request, 'users/createprofile.html')

def seller_profile(request, id):
    seller=User.objects.get(id=id)
    context={
        'seller': seller,

    }
    return render(request, 'users/sellerprofile.html',context)
