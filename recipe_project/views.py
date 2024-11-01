from django.shortcuts import render, redirect
#Django authentication libraries
from django.contrib.auth import authenticate, login
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest

# define a function view called login_view that takes a request from the user
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
            username=form.cleaned_data.get('username')      #read username
            password=form.cleaned_data.get('password')    #read password

            #use Django authenticate function to validate the user
            user=authenticate(username=username, password=password)
            if user is not None:                    #if user is authenticated
                #then use pre-defined Django function to login
                login(request, user)
                return redirect('recipes:list') #& send the user to desired page
        else:                                               #in case of error
            error_message ='ooops.. something went wrong'   #print error message

    #prepare data to send from view to template
    context ={
        'form': form,                                 #send the form data
        'error_message': error_message                     #and the error_message
    }

    #load the login page using "context" information
    return render(request, 'auth/login.html', context)
    

#define a function view called logout_view that takes a request from user
def logout_view(request: HttpRequest):
    logout(request)
    return redirect('logout_success')

def logout_success(request):
    return render(request, 'auth/success.html')