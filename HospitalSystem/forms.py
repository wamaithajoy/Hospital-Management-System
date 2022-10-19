from django import forms
from HospitalSystem.models import Appointmnet, Doctor, Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"  

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointmnet
        fields="__all__"                         

