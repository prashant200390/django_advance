from django.shortcuts import render, get_object_or_404, redirect
from .forms import studentForm
from .models import Student
# Create your views here.

def student_create(request):
    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
    return render(request,'student_form.html',{'form':form})

def student_list(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{'students':students})

def student_detail(request,pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request,'student_detail.html',{'student':student})

def student_edit(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == "POST":
        form = studentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = studentForm(instance=student)
    return render(request,'student_form.html',{'form':form})

def student_delete(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request,'student_conform_delete.html',{'student':student})