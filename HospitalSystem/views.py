from django.shortcuts import render

def home_page(request):
    return render(request,"home_page.html")

def about_page(request):
    return render(request,"about_page.html")    

# Create your views here.
