from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def index(request):
    if request.method=="POST":
        nm=request.POST["name"]
        em=request.POST["email"]
        ph=request.POST["phone"]
        jd=request.POST["joining"]
        jr=request.POST["job"]
        print(nm,em,ph,jd,jr)
        obj=Employee.objects.create(name=nm,email=em,phone=ph,joining=jd,job=jr)
        obj.save()
        return HttpResponse('your Data Saved Successfully...!')
    return render(request,'index.html')


def showdata(request):
    employees=Employee.objects.all()
    print(employees)
    context={}
    context["employees"]=employees
    for i in employees:
        print(i.name,i.email,i.phone,i.job,i.joining)
    return render(request,'home.html',context)

def delete_data(request,eid):
    employee=Employee.objects.get(id=eid)
    print(employee.name)
    employee.delete()

    return render('/showdata')

def edit(request,sid):
    context={}
    if request.method=='GET':
        employee=Employee.objects.get(id=sid)
        context["employee"]=employee
        return render (request,'update.html',context)
    elif request.method=="POST":
        nm=request.POST["name"]
        em=request.POST["email"]
        ph=request.POST["phone"]
        jd=request.POST["joining"]
        jr=request.POST["job"]

        employee1=Employee.objects.filter(id=sid)
        employee1.update(name=nm,email=em,phone=ph,joining=jd,job=jr)
        return redirect('/home')


