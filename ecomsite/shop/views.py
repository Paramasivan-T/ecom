from django.shortcuts import render, redirect
from .models import Order, Product
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url= 'login')
def index(request):
    product_objects = Product.objects.all()

    #Search Code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name != None:
        product_objects = product_objects.filter(title__icontains=item_name)

    #paginator Code
    paginator = Paginator(product_objects, per_page=4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})

@login_required(login_url= 'login')
def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object':product_object})

@login_required(login_url= 'login')
def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        address2 = request.POST.get('address2', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip = request.POST.get('zip', "")
        total = request.POST.get('total', "")

        order = Order(total=total,items=items,name=name, email=email, address=address, address2=address2, city=city, state=state, zip=zip)
        order.save()

    return render(request, 'shop/checkout.html')
    
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request=request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username Or Password is incorrect')
                
        context={}
        return render(request, 'shop/login.html', context)
    
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"Account Successfully Created for {username}")
                return redirect('login')
        
        context={'form': form}
        return render(request, 'shop/register.html', context)
    
@login_required(login_url= 'login')
def logoutUser(request):
    logout(request)
    return redirect('login')