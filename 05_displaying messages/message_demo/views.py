from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def show_message(request):
    messages.debug(request,'this is a debug message.')
    messages.info(request,"this is a info message")
    messages.success(request,"this is a success message")
    messages.warning(request,"this is a warning message")
    messages.error(request,"this is a error message")
    
    return render(request,'showMessage.html')