from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Department,Doctors

from .forms import BookingForm
# Create your views here.

def index(request):  
    return render(request,'index.html')

def about(request):  
    return render(request,'about.html')


def bookdoctos(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form = BookingForm()
    dict_form = {

        'form':form
    }
    return render(request,'bookfdoc.html',dict_form)

def doc(request):
    dict_docs={
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def department(request):
    dict_dpt={
        'dept': Department.objects.all()
    }
    return render(request,'department.html',dict_dpt)

def contact(request):
    return render(request,'contact.html')

