# here we have imported all the classes which we are going to use in our file views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from .models import rent1payee
from .models import Rentyourhouse
from .models import Feedback

from .forms import ImageForm

from .models import Image 



# Create your views here.

# this function index is to connect our app first to the file index.html which is present in the folder templates
# under the project tenant
def index(request) :
    comments=Feedback.objects.all()
    return render(request,"index.html",{'comments':comments})

# this function register is to connect our app first to the file register.html which is present in the folder  
# templates under the project tenant
#  here  we are transerfering the data to the database tenant3 
def register(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # by writing this condition we are checking that if password1 and password2 are equal or not 
        if password1==password2 :
            # by writing this condition we are checking that if this username is already registered or not
            if User.objects.filter(username=username).exists() :
               messages.info(request,'Username Taken')
               return redirect('register')
            # by writing this condition we are checking that if this email is already registered or not
            elif User.objects.filter(email=email).exists() :
               messages.info(request,'email taken already')
               return redirect('register')
            else :
                user =User.objects.create_user(username=username,email=email,password=password1)
                # by writing this only we are hitting the database to store the information
                user.save();
                print('user created')
                return redirect('login') 
        else :
            messages.info(request,'password not matching')
            return redirect('register')
        return('/')  
    else :
           return render(request,"register.html")

  

# this function login is to connect our app first to the file login.html which is present in the folder  
# templates under the project tenant
#  here  we are transerfering the data to the database tenant3 
def login(request) :
     if request.method == 'POST' :
         username = request.POST['username']
         password = request.POST['password']
          # by writing this we are checking whether the entered username and password are of the same user or not 
         user = auth.authenticate(username=username,password=password)
         if user is not None :
             request.session['member_id'] = user.id
             auth.login(request,user)
             return redirect('/')
         else :
             messages.info(request,'invalid credentials')
             return redirect('login')
            
     else :
         return render(request,"login.html")

# this function is to take out the user from the site
def logout(request) :
    auth.logout(request)
    request.session['member_id'] = 0
    return redirect('/')
   
# by writing we are applying the condition that if user is logged in then only call booking function
@login_required(login_url='login')
# this function booking is to connect our app first to the file booking.html which is present in the folder  
# templates under the project tenant
def booking(request):
    return render(request,"booking.html")


# by writing we are applying the condition that if user is logged in then only call rent function
@login_required(login_url='login')
# this function booking is to connect our app first to the file rent.html which is present in the folder  
# templates under the project tenant
def rent(request):
    return render(request,"rent.html")


# this function booking is to connect our app first to the file about.html
def about(request) :
    return render(request,"about.html")  


# this function FAQ is to connect our app first to the file FAQ.html
def FAQ(request) :
    return render(request,"FAQ.html")


# by writing we are applying the condition that if user is logged in then only call booking2 function
@login_required(login_url='login')
def booking2(request):
    p_email=request.POST['p_email']
    p_name=request.POST['p_name']
    p_country=request.POST['p_country']
    Rentpayee=rent1payee(p_email=p_email,p_name=p_name,p_country=p_country)
    Rentpayee.save();



# by writing we are applying the condition that if user is logged in then only call rentyourhouse function

# this function rentyourhouse  is to connect our app first to the booking.html
@login_required(login_url='login')
def rentyourhouse(request) :
    fullname = request.POST["fullname"]
    From = request.POST["From"]
    To = request.POST["To"]
    adults =request.POST["adults"]
    children =request.POST["children"]
    phonenumber= request.POST["phonenumber"]
    appointment = request.POST["appointment"]
    roomdescription = request.POST["roomdescription"]
    tenantdescription = request.POST["tenantdescription"]
    price = request.POST["price"]
    houselocation=request.POST["houselocation"]
    localitylocation=request.POST["localitylocation"]
    citylocation=request.POST["citylocation"]
    RENTYOURHOUSE = Rentyourhouse(fullname=fullname,From=From,To=To,adults= adults,children=children,phonenumber=phonenumber,appointment=appointment,roomdescription=roomdescription,tenantdescription =tenantdescription,price=price,houselocation=houselocation,localitylocation=localitylocation,citylocation=citylocation)
    # by writing this only we are hitting the database to store the information
    RENTYOURHOUSE.save();
    return render(request,"booking.html")


# by writing we are applying the condition that if user is logged in then only call feedback function
@login_required(login_url='login')
def feedback(request) :
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    feed = Feedback(name=name,email=email,subject=subject,message=message)
    # by writing this only we are hitting the database to store the information
    feed.save();
    
    return redirect('index')


# this function showimage is to get an image from the user
def showimage(request):
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = ImageForm() 
    return render(request, 'hotel_image_form.html', {'form' : form})


# this function success is to show that the image is successfully uploaded
def success(request): 
    return HttpResponse('successfully uploaded') 


# by writing we are applying the condition that if user is logged in then only call rent function
@login_required(login_url='login')
# this function rent is to connect our app first to the file rent.html
def rent(request):
    if request.method== 'POST':

        request.session['first']=True
        return redirect('rent2')
    else:
        return render(request,"rent.html")

# by writing we are applying the condition that if user is logged in then only call rent2 function
@login_required(login_url='login')
# this function rent2  is to connect our app first to the file rent2.html
def rent2(request):
    if request.session['first']=='True':
        request.session['first']=False
        q= Rentyourhouse.objects.all()
        return render(request,"rent2.html",{'q':q})
        
    else:
        q= Rentyourhouse.objects.filter()
        return render(request,"rent2.html",{'q':q})