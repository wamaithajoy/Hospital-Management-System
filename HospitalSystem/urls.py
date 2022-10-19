from django.urls import path
from . import views
 
urlpatterns = [
    path("home/",views.home_page,name="home"),
    path("about/",views.about_page,name="about"),
    path("patientForm",views.patient_Form,name="patientForm"),
    path("doctorForm",views.doctor_Form,name="doctorForm"),
    path("service",views.service_page,name="service"),
    path("contact",views.contact_page,name="contact"),
    path("appointment",views.appointment_Form,name="appointment"),
    path("records",views.records_page,name="records"),

]
