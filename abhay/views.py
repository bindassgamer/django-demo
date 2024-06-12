from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from database.models import Profile,add_expense,UserModel



def home(request):
    return render(request,'app/index.html')

def main(request):
    expenseData=add_expense.objects.all()
    data={
        'ExpData':expenseData
    }
    if request.method=='POST':
        # select = request.POST.get('select')
        name=request.POST.get('name')
        category=request.POST.get('category')
        date=request.POST.get('date')
        amount=request.POST.get('amount')
        type=request.POST.get('select')
        print(type)
        if type == '0': 
            type = "Expense"
        else:
            type = "Income"
        en=add_expense(name=name,category=category,date=date,amount=amount,type=type)
        en.save()
    
    
    return render(request,'app/demo.html',data)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request,'Username Does not exists')
            return redirect('login')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Wrong Password')
            return redirect('login')
        else:
            login(request ,user)
            return redirect("main")
    return render(request,'app/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        location = request.POST.get('location')
        contact = request.POST.get('contact')

        print(username,email,password1,password2,location,contact)
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'Username Already exists')
            return redirect('register')
        user = User.objects.create(
            username = username,
        )
        user.set_password(password1)
        user.save()
        messages.success(request,'Account created successfully')
        return redirect('login')
    return render(request,'app/register.html')

def profile(request):
    if request.POST:
        print("post hua")
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            print("validate hua")
            u_form.save(force_insert=False)
            p_form.save(force_insert=False)
            messages.success(request,'Account has been updated successfully')
            print('suz')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'app/profile.html',context)


