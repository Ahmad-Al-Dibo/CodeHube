from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import logout

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already signed in.")
        return redirect("index")

    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        remember = form.cleaned_data['remember']
        
        user = authenticate(request, email=email, password=password) 
        if user:
            login(request, user)
            if not remember:
                request.session.set_expiry(0) # Session expires on browser close
            messages.success(request, "Successfully logged in.")
            return redirect('profile')
        else:
            form.add_error(None, "Invalid email or password")
    return render(request, 'account/login.html', {'form': form})




def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are signed in. Logout to register an account.")
        return redirect("index")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(request, "Successfully registered.")
        return redirect('login')
    return render(request, 'account/register.html', {'form': form})


def logout_view(request):
    logout(request)  
    messages.success(request, "Successfully logged out.")
    return redirect('index')  

