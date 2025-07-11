from django.shortcuts import render,redirect,get_object_or_404

from .forms import StudentForm,RegisterForm
from .models import Student

def student_list(request):
    Students=Student.objects.all()
    return render(request,'studentlist.html',{'Students':Students})

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
        
