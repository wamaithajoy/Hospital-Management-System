from django.shortcuts import render,redirect
from HospitalSystem.forms import DoctorForm, PatientForm

def home_page(request):
    return render(request,"home_page.html")

def about_page(request):
    return render(request,"about_page.html")   

def patient_Form(request):
    if request.method=="POST":

        form=PatientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("service")
        else:
            print(form.errors)
    else:
        form=PatientForm()

    return render(request,"patient_Form.html",{"form":form}) 

def service_page(request):
    return render(request,"service_page.html")  

def doctor_Form(request):
    if request.method=="POST":

        form=DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("service")
        else:
            print(form.errors)
    else:
        form=DoctorForm()

    return render(request,"doctor_Form.html",{"form":form})

def contact_page(request):
    return render(request,"contact_page.html")       


# Create your views here.
