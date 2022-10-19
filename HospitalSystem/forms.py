from django import forms
from HospitalSystem.models import Doctor, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"                   

