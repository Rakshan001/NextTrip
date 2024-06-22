from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')  #used decorators library to overcome the direct access of the Home page without login in after applying decorator we can not directly go into home page with search bar it require login information
def HomePage(request):
    return render(request, 'loginpage/home.html')
#return HttpResponse("This is the home page")

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        print(uname,email,pass1,pass2)

        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists. Please choose a different username.")

        # Check if passwords match
        if pass1 != pass2:  #checks constraints it create the database only if it meet requirement else it will not create the database
            return HttpResponse("Passwords do not match. Please try again.")
        else:
            # Create a new user
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            # return HttpResponse("Login succesfull")
            return redirect('login')  #redirect into login page

    return render(request,'loginpage/signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")


    return render(request,'loginpage/login.html')
    

def search_buses(request):
    return render(request, 'nextbus/search_form.html')




def LogoutPage(request):
    logout(request)
    return redirect('login')



def HomePage(request):
    username = request.user.username  # Access the username
    return render(request, 'loginpage/home.html', {'username': username})

def search_buses(request):
    username = request.user.username
    return render(request, 'nextbus/search_form.html', {'username': username})
