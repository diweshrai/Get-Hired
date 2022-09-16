from dataclasses import fields
from pyexpat import model
from django import forms
from dashboard.models import Resume
from . models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description'] 

class DateInput(forms.DateInput):
    input_type = 'date'
    
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets ={'due':DateInput()}
        fields =['subject','title','description','due','is_finished'] 
                
       
        
class Post(forms.ModelForm):
    class Meta:
        model = vac
        widgets ={'due':DateInput()}
        fields =['company','designation','about','due','is_finished']  
        
        
        
        
        
        
class student_profile(forms.ModelForm):
    class Meta:
        model = s_prof
        widgets ={'dob':DateInput()}
        fields =['s_name','roll_no','dob','edu','email','s_no','T_add','post_code']               
        
        
        

class DashboardFom(forms.Form):
    text = forms.CharField(max_length=100,label="Enter Your Search :") 

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']   

class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices = CHOICES,widget= forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Number'} 
    )) 
    measure1 = forms.CharField(
        label='',widget = forms.Select(choices = CHOICES)    
    ) 
    measure2 = forms.CharField(
        label='',widget = forms.Select(choices = CHOICES)
    )

class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Number'} 
    )) 
    measure1 = forms.CharField(
        label='',widget = forms.Select(choices = CHOICES)    
    ) 
    measure2 = forms.CharField(
        label='',widget = forms.Select(choices = CHOICES)
    )    


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
        
        
        
        
        
        

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

JOB_CITY_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Pune', 'Pune'),
 ('Ranchi', 'Ranchi'),
 ('Mumbai', 'Mumbai'),
 ('Dhanbad', 'Dhanbad'),
 ('Banglore', 'Banglore')
]

class ResumeForm(forms.ModelForm):
 gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
 job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
 class Meta:
  model = Resume
  fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'my_file']
  labels = {'name':'Full Name', 'dob': 'Date of Birth', 'pin':'Pin Code', 'mobile':'Mobile No.', 'email':'Email ID', 'my_file':'Document'}
  widgets = {
   'name':forms.TextInput(attrs={'class':'form-control'}),
   'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   'locality':forms.TextInput(attrs={'class':'form-control'}),
   'city':forms.TextInput(attrs={'class':'form-control'}),
   'pin':forms.NumberInput(attrs={'class':'form-control'}),
   'state':forms.Select(attrs={'class':'form-select'}),
   'mobile':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
  }        
  
  
  
  
class appnow(forms.ModelForm):
    class Meta:
        model = Appnow
        fields = ['jobid','username','name','roll_no','mobile_no','my_file']