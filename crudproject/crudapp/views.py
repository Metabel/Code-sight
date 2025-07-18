from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import StudentForm,RegisterForm
from .models import Student
from django.contrib.auth import login,logout



def student_list(request):
    Students=Student.objects.all()
    return render(request,'studentlist.html',{'Students':Students})
@login_required
@staff_member_required
def add_student(request):
    form=StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
        
    return render(request,'studentform.html',{'form':form})

# Create your views here.

#update
def update_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    form=StudentForm(request.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'studentform.html',{'form':form})
#DELETE
def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect('student_list')

def register(request):
    if request.method =='POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=RegisterForm()  
        
    return render(request,'register.html',{'form':form})
def login_user(request):
    if request.method =='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('student_list')
        else:
            messages.error(request,"invalid username or password")
    else:
        form=AuthenticationForm() 
       
    return render(request,'login.html',{'form':form})
def logout_user(request):
    logout(request)
    return redirect('login')

    
    
        
