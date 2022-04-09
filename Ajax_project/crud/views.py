from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def index(request):
    form = EmployeeForm()
    employee = Employee.objects.all()
    #print(employee)
    context = {
        'form': form,
        'employee': employee
    }
    return render(request, 'index.html', context)

def save_data(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp_id = request.POST.get('eid')
            name = request.POST['name']
            age = request.POST['age']
            address = request.POST['address']
            salary = request.POST['salary']

            if emp_id == '':
                employee = Employee(name=name, age=age, address=address, salary=salary)
            else:
                employee = Employee(id = emp_id, name=name, age=age, address=address, salary=salary)

            #print(employee)
            employee.save()
            employee = Employee.objects.values()
            #print(employee)     
            print("______")       
            employee_data = list(employee) ### Because python object is not iterable so converted into list
            print(employee_data)
            return JsonResponse({'status': 'Save', 'employee_data':employee_data })
    else:
        return JsonResponse({'status': 0})



def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print(id)
        employee = Employee.objects.get(pk=id)
        employee_data = {"id": employee.id, "name": employee.name, "age": employee.age, "address": employee.address, "salary": employee.salary}
        print(employee_data)
        return JsonResponse(employee_data)

    


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        employee = Employee.objects.get(pk=id)
        employee.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})