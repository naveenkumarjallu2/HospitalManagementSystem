from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from HospitalApp.models import Diseases, City, Patient


# Create your views here.
def reg_fun(request):
    return render(request,'register.html',{'data':''})


def regdata_fun(request):
    user_name = request.POST['txtName']
    user_email = request.POST['txtEmail']
    user_pswd = request.POST['txtPwd']

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'register.html',{'data':'User name and Email already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name,email=user_email,password=user_pswd)
        u1.save()
        return redirect('log')


def log_fun(request):
    return render(request,'login.html',{'data':''})


def logdata_fun(request):
    user_name = request.POST['txtName']
    user_pswd = request.POST['txtPwd']
    user1 = authenticate(username=user_name,password=user_pswd)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not a superuser'})
    else:
        return render(request,'login.html',{'data':'Enter proper username and password'})



def home_fun(request):
    return render(request,'home.html')


def addpatient_fun(request):
    city = City.objects.all()
    diseases = Diseases.objects.all()
    return render(request,'addpatient.html',{'City_Data':city,'Diseases_Data':diseases})



def readdata_fun(request):
    s1 = Patient()
    s1.Patient_Name = request.POST['txtName']
    s1.Patient_Age = request.POST['txtAge']
    s1.Patient_Phone = request.POST['txtPhone']
    s1.Patient_City = City.objects.get(City_Name=request.POST['ddlCity'])
    s1.Patient_Diseases = Diseases.objects.get(Diseases_Name=request.POST['ddlDiseases'])
    s1.save()
    return redirect('add')

def display_fun(request):
    s1 = Patient.objects.all()
    return render(request,'display.html',{'data':s1})



def update_fun(request,id):
    s1 =Patient.objects.get(id=id)
    city = City.objects.all()
    course = Diseases.objects.all()
    if request.method == 'POST':
        s1.Patient_Name = request.POST['txtName']
        s1.Patient_Age = request.POST['txtAge']
        s1.Patient_Phone = request.POST['txtPhone']
        s1.Patient_City = City.objects.get(City_Name=request.POST['ddlCity'])
        s1.Patient_Diseases = Diseases.objects.get(Diseases_Name=request.POST['ddlDiseases'])
        s1.save()

        return redirect('display')
    return render(request,'update.html',{'data':s1,'City_Data':city,'Diseases_Data':course})


def delete_fun(request,id):
    s1 = Patient.objects.get(id=id)
    s1.delete()
    return redirect('display')


def log_out_fun(request):
    return redirect('log')