from django.urls import path
from . import views
 
urlpatterns = [
    path("home/",views.home_page,name="home"),
    path("about/",views.about_page,name="about"),

]
