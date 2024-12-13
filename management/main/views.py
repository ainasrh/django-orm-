from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import login_form,project_form,reg_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import project,employee
from django.db.models import Q

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    if 'search_data' in request.GET:
        search=request.GET['search_data']
        data=project.objects.filter(Q(task__icontains =search) | Q(assigned_To__name__icontains=search) | Q(status__icontains=search) | Q(priority__icontains=search))
    else:
        data=project.objects.prefetch_related('assigned_To')

    return render(request,'home.html',{'data':data})

def register(request):
    if request.method=='POST':
        form=reg_form (request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=User(username=username,password=password)
            user.set_password(password)
            user.save()
            return redirect('login')
    else:      
        form=reg_form()
    return render(request,'register.html',{'form':form})

def log_in(request):
    error=' '
    
    if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')  
            else:
                error='check your password or username  '
                   
    form=AuthenticationForm()
    
    return render(request,'login.html',{'form':form,'error':error})

def log_out(request):
    logout(request)
    return redirect('login')

def create(request):
    # succes=''
    if request.method=='POST':
        form=project_form(request.POST)
        if form.is_valid():
            form.save()
            # succes='task assembled succesfully'
            return redirect('home')
       
        
    form=project_form()
    return render(request,'create.html',{'form':form}   )

def update(request,id):
    upd=project.objects.get(id=id)
    form=project_form(instance=upd)
    context={'form':form}
    if request.method=='POST':
        form=project_form(request.POST,instance=upd)
        if form.is_valid():
            form.save()
            # succes='task assembled succesfully'
            return redirect('home')
    

    return render(request,'create.html',context)

def delete_view(request,id):
    data=project.objects.get(id=id)
    data.delete()
    return redirect('home')