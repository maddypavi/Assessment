from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from employee.forms import EmployeeForm  
from employee.models import Employee  
 
  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
                form.save()  
                return redirect('show')  
        
    else:  
        form = EmployeeForm()  
    return render(request,'view.html',{'form':form})

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("show")
