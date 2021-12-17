from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.
def AddView(req):
    form = LaptopModelForm()
    if req.method == 'POST':
        form = LaptopModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show_lap')
    context = {'form':form}
    return render(req,'add_laptop.html',context)


def ListView(request):
    laptop_list = Laptop.objects.all()
    template_name = "show_laptop.html"
    context = {'laptop_list': laptop_list}
    return render(request, template_name, context)

def updateView(request,i):
    laptop = Laptop.objects.get(id=i)
    form = LaptopModelForm(instance=laptop)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect("show_lap")
    template_name = "add_laptop.html"
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request,i):
    laptop = Laptop.objects.get(id=i)
    laptop.delete()
    return redirect("show_lap")
