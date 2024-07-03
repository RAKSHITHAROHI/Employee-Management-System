from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Employee
from .forms import EmployeeForm

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def add(request,a,b):
    c=a+b
    return HttpResponse('The addition of 2 numbers is'+str(c))

def Employee_list(request):
    Employees=Employee.objects.all()

    return render(request,'Employee_list.html',{'Employees':Employees})

def AddEmployee(request):
    if(request.method=='POST'):
        form=EmployeeForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect(Employee_list)
    else:
        form=EmployeeForm()
        return render(request,'AddEmployee.html',{'form':form})

def EditEmployee(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            employee=form.save()
            return redirect(Employee_list)
    else:
        form = EmployeeForm(instance=employee)
        return render(request, "AddEmployee.html", {'form': form})



def DeleteEmployee(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    employee.delete()
    return redirect(Employee_list)
