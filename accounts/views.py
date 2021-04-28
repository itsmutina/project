from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Customer
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='login')
#@allowed_users(allowed_roles=['Admin'])
def home(request):
    
    balances = Customer.objects.all()
    
    #balances = Customer.objects.get(name = "wilmot2")
   # wilmot2 = balances.balance
    #withdraw = balances.withdrawn

    context = {
        'balances':balances,
       # 'wilmot2':wilmot2,
       # 'withdraw': withdraw

    }
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def earn(request):
    return render(request, 'accounts/earn.html')


@login_required(login_url='login')
def withdraw(request):
    return render(request, 'accounts/withdraw.html')


def withdrawconfirm(request):
    return render(request, 'accounts/withdrawlconfirm.html')

@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')

            else: messages.info(request, 'Invalid crintentials')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


#@unauthenticated_user
def registerPage(request):
    #customer_id = request.session.get('ref_profile')
    #print('customer_id,' customer_id)
    form = CreateUserForm 

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
                #if customer_id is not None:
                   # recommended_by_profile = Customer.objects.get(id=customer_id)
                    #instance = form.save()
                    #registered_user = User.objects.get(id = instance.id)
                    #registered_profile = Customer.objects.get(name = registered_user)
                    #registered_profile.recommended_by = recommended_by_profile
                    #registered_profile.save()
                #else:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for'  + user)
            return redirect('login')

        context={
            'form':form
        }
        return render(request, 'accounts/register.html', context)

