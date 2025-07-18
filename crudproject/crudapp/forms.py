from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth .models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =['fullname', 'age' ,'course']
        widgets ={
            'fullname':forms.TextInput(attrs={'class':'form-control border-primary'}),
            'age':forms.NumberInput(attrs={'class':'form-control border-primary'}),
            'course':forms.TextInput(attrs={'class':'form-control border-primary'}),  
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]  
        
        