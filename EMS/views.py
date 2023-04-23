from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Employees

# Create your views here.
def home(request):
    emp1 = Employees.objects.all()
    count = 0 
    for e in emp1:
        if e.Active == True:
            count += 1
    emp = len(Employees.objects.all())
    return render(request,"home.html",{'emp':emp,'count':count})

def Create(request):
    if request.method == "POST":
        Name = request.POST['Name']
        DOB = request.POST['DOB']
        DOJ = request.POST['DOJ']
        Department = request.POST['Department']
        Post = request.POST['Post']
        Address =  request.POST['Address']
        City = request.POST['City']
        Country =  request.POST['Country']
        Zipcode  = request.POST['Zipcode']
        State = request.POST['State']
        if Name == "":
            messages.info(request,"Please Enter the Name field")
            return redirect("/Create")
        if DOB == "":
            messages.info(request,"Please Enter the DOB field")
            return redirect("/Create")
        if DOJ == "":
            messages.info(request,"Please Enter the DOJ field")
            return redirect("/Create")
        if Department == "":
            messages.info(request,"Please Enter the Department field")
            return redirect("/Create")
        if Post == "":
            messages.info(request,"Please Enter the Post field")
            return redirect("/Create")
        if Address == "":
            messages.info(request,"Please Enter the Address field")
            return redirect("/Create")
        if City == "":
            messages.info(request,"Please Enter the City field")
            return redirect("/Create")
        if Country == "":
            messages.info(request,"Please Enter the Country field")
            return redirect("/Create")
        if Zipcode == "":
            messages.info(request,"Please Enter the Zipcode field")
            return redirect("/Create")
        if State == "":
            messages.info(request,"Please Enter the State field")
            return redirect("/Create")
        else:   
            Emp = Employees(Name = Name,DOB = DOB,DOJ = DOJ,Department = Department,Post = Post,Address = Address,City = City,Country = Country,Zipcode = Zipcode,State = State)
            Emp.save()
            print('user Created')
            return redirect('/Employee')   
    else:
        return render(request,"create.html")

def Employee(request):
    
    Emp = Employees.objects.all()
    
    return render(request,"employee.html",{'Emp':Emp})

def onLeave(request):
    Emp = Employees.objects.all()
    di = {}
    for i in Emp:
        if i.Active == True:
            di[i] = Emp
    print(di)
    return render(request,'onLeaveEmployee.html',{'Emp':di})        

def EmployeeDetails(request,id):
    filteredData = Employees.objects.filter(id = id)
    return render(request,"employeeDetails.html",{'Details' : filteredData})

def EditEmployee(request,id):
    data = Employees.objects.filter(id=id)   
    return render(request,"EditEmployee.html",{'Data':data})

def update(request,id):
    if request.method == "POST":
        Name = request.POST['Name']
        DOB = request.POST['DOB']
        DOJ = request.POST['DOJ']
        Department = request.POST['Department']
        Post = request.POST['Post']
        Address =  request.POST['Address']
        City = request.POST['City']
        Country =  request.POST['Country']
        Zipcode  = request.POST['Zipcode']
        State = request.POST['State']
        emp = Employees(id = id,Name = Name,DOB = DOB,DOJ=DOJ,Department = Department,Post = Post,Address = Address,City = City,Country = Country,Zipcode = Zipcode,State = State)
        emp.save()
        return redirect('/Employee')
    return render(request,"EditEmployee.html")


def deleteEmployee(request,id):
    data = Employees.objects.get(id= id)
    data.delete()
    print(data)
    return redirect('Employee')



def update_object(request, id):
    obj = get_object_or_404(Employees,id=id)
    obj.Active = True
    obj.save()
    return redirect('Employee')


def update_object1(request, id):
    obj = get_object_or_404(Employees,id=id)
    obj.Active = False
    obj.save()
    return redirect('Employee')