from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login as django_login

# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username ,password=password)
            
            if user is not None:
                django_login(request,user)
                return render(request, "index.html",{})
            else:
                return render(request, "cuentas/login.html",{"forms":form})
        else:
            return render(request, "cuentas/login.html",{"forms":form})
                
                
                
        
        
    form = AuthenticationForm()
    return render(request, "cuentas/login.html",{"form": form})

def register(request):
       
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "index.html",{})
            else:
                return render(request, "cuentas/register.html",{"form":form})

        form = UserCreationForm()
        return render(request, "cuentas/register.html",{"form":form})