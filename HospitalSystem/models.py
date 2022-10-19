from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    date_of_birth=models.DateField(max_length=10,null=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),

    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    contact=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=45,null=True)
    address=models.CharField(max_length=20,null=True)
    MARITAL_CHOICES=(
        ('Single','Single'),
        ('Married','Married'),
    )
    marital_status = models.CharField(max_length=10,choices=MARITAL_CHOICES,null=True)
    MEDICATION_CHOICE=(
        ('yes','yes'),
        ('no','no'),
    )
    Taking_any_medications_currently= models.CharField(max_length=10,choices=MEDICATION_CHOICE,null=True)
    if_yes_please_list_below= models.TextField(max_length=10,null=True)

class Doctor(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=45,null=True)
    contact=models.CharField(max_length=15,null=True)
    address=models.TextField(max_length=20,null=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),

    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    COUNTY_CHOICES=(
        ('Nairobi','Nairobi'),
        ('Nakuru','Nakuru'),
        ('Nyeri','Nyeri'),
        ('Muranga','Muranga'),
        ('Kakamega','Kakamega'),
        ('Kirinyaga','Kirinyaga'),
        ('Kisumu','Kisumu'),
    )
    county = models.CharField(max_length=20, choices=COUNTY_CHOICES,null=True)
    SPECIALIZATION_CHOICES=(
        ('Neurologist','Neurologist'),
        ('Dentist','Dentist'),
        ('ENT','ENT'),
        ('Oncologist','Oncologist'),
        ('Cardiologist','Cardiologist'),
        ('Eye Specialist','Eye Specialist'),
        ('Orthopedic','Orthopedic'),
        ('Gynecologist','Gynecologist'),
        ('Dermatologist','Dermatologist'),
        ('Opthamologists','Ophamologist'),
        ('Other','Other'),
    )
    specialization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES,null=True)
    WORKTYPE_CHOICES=(
        ('Fulltime','Fulltime'),
        ('Parttime','Partime'),
        ('Remote','Remote'),
    )
    work_type = models.CharField(max_length=20, choices=WORKTYPE_CHOICES,null=True)




   
    

  
  