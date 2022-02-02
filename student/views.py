from django.shortcuts import redirect, render
from student.forms import StudentForm

from student.models import Student

# Create your views here.

def home(request):
    return render(request,"student/home.html")

def student_list(request):
    students = Student.objects.all()

    context ={
        "students":students
    }
    return render(request,"student/student_list.html",context)

def student_add(request):
    form = StudentForm()
    
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")


    context={
        "form":form
    }
    return render(request,"student/student_add.html",context)
 
def student_detail(request,id):
    student = Student.objects.get(id=id)

    context = {
        "student":student
    }
    return render(request,"student/student_detail.html",context)


def student_update(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method =="POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form":form
    } 
    return render(request,"student/student_update.html",context)

def student_delete(request,id):
    student = Student.objects.get(id=id)
    if request.method =="POST":
        student.delete()
        return redirect("list")
    context = {
        "student":student
    }
    
    return render(request,"student/student_delete.html",context)