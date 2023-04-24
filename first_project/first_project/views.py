from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import datetime

def home(request):
    isActive = True
    if request.method=='POST':
        val = request.POST.get("check")
        print(val)
        if val:
            isActive = True
        else:
            isActive = False

    today=datetime.date
    # print("hello")

    name="Mohit soni"
    list_of_program=[
        "wap a program to find prime no",
        "wap a program to print prime no between 1 to 100",
        "wap a program to print integer"
    ]
    student_data={
        'student_name':"Mohit Soni",
        'student_college':"Sgi",
        'student_mail':"mohitsonims04@gmail.com",
        'student_mobile': "7728852301",
    }
    data={
        'name':name,
        'isActive': isActive,
        'list_of_program':list_of_program,
        'today':today,
        'student_data':student_data,
    }


    return render(request,"home.html",data)


def contact(request):
    print("hello")
    # return HttpResponse("<h1>You have scuessfully done<h1>")
    return render(request, "contact.html", {})


def about(request):
    print("hello")
    # return HttpResponse("<h1>You have scuessfully done<h1>")
    return render(request, "about.html", {})
