from django.shortcuts import render, redirect
#Django authentication libraries
from django.contrib.auth import authenticate, login, logout
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.contrib import messages


# LOGIN VIEW
def login_view(request: HttpRequest):
    #initialize:
    error_message = None
    #form object with username and password fields
    form = AuthenticationForm
# When user hits "login" button, then POST request is generated
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        #read the data sent by the form via POST request
        if form.is_valid():                                
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            #use Django authenticate function to validate the user
            user=authenticate(username=username, password=password)
            if user is not None:                         #if user is authenticated
                #then use pre-defined Django function to login
                login(request, user)
                return redirect('recipes:list')          # send the user to desired page
        else: 
            error_message ='ooops.. something went wrong'
    # Initialize registration form for the moal
    register_form = UserCreationForm()
    # Initialize data to utilize in template
    context ={
        'form': form, 
        'register_form': register_form,
        'error_message': error_message
    }
    # load the login page using "context" information
    return render(request, 'auth/login.html', context)


# REGISTER VIEW
def register_view(request: HttpRequest):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        register_form.fields['username'].help_text = ''
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        register_form = UserCreationForm()
    #re-render login page with both login and registration forms
    return render(request, 'auth/login.html', {
        'form': AuthenticationForm(),
        'register_form' : register_form
    })
    

# LOGOUT VIEW
def logout_view(request: HttpRequest):
    logout(request)
    return redirect('logout_success')

def logout_success(request):
    return render(request, 'auth/success.html')