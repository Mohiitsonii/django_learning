from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Emp

def employee_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{
        'emps':emps
    })


def add_emp(request):
    if request.method=="POST":
        name=request.POST.get("emp_name")
        id=request.POST.get("emp_id")
        phone=request.POST.get("emp_phone")
        address = request.POST.get("emp_address")
        status = request.POST.get("emp_status")
        department = request.POST.get("emp_department")
        e=Emp()
        e.name = name
        e.emp_id = id
        e.phone=phone
        e.address = address
        e.department = department
        if status is None:
            e.working =False
        else:
            e.working = True
        e.save()
        
        print("data is coming ")
        return redirect("/employee")
    return render(request,"emp/add_emp.html",{})

def del_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/employee")
