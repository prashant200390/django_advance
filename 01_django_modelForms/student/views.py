from django.shortcuts import render
from .forms import studentForm
# Create your views here.

def student_create(request):
    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
    return render(request,'student_form.html',{'form':form})