from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from .forms import  *
from .models import *
from django.contrib import messages
from django.urls import reverse

def index (request):
    if request.method=='GET':
        form=TodoForm()      
        return render(request,'index.html',{'form':form}) 
    elif  request.method=='POST':
        form= TodoForm(request.POST) 
        if form.is_valid():
            new_to_to_item=form
            new_to_to_item.save()
            return redirect("all")
 

def all (request):
    all_to_do=TO_DO.objects.all().order_by("-date")
    
    return render(request,'all.html',{"all_to_do":all_to_do})


def delete_item(request,item_id):
    all_to_do=TO_DO.objects.all().order_by("-date")
    item = TO_DO.objects.get(id=item_id)
    item.delete()
    return redirect("all")


def edit_item(request,id_item):
    obj = TO_DO.objects.get(id=id_item)
    mydictionary = {
        "text" : obj.text,
        "date" : obj.date,
        "id" : obj.id,
        
    }
    
    print("dcdckdc")
    return render(request,'edit.html',context=mydictionary)


def update_item(request,id_item):
    print("updateeeeeeeeeeeeeeeee")
    obj = TO_DO(id=id_item)
    obj.text = request.GET['text']
    obj.ddate = request.GET['date']    
    obj.save()
    print("updateeeeeeeee")
    mydictionary = {
        "alltodos" : TO_DO.objects.all()
    }
    return render(request,'all.html',context=mydictionary)

