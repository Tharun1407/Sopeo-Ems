from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Employees

# Home Page of The Web site
def home(request):
    emp1 = Employees.objects.all()
    count = 0 
    for e in emp1:
        if e.Active == False:
            count += 1
    emp = len(Employees.objects.all())
    return render(request,"home.html",{'emp':emp,'count':count})




# Create Employee View : 

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

#List Of Employees Page View:

def Employee(request):
    Emp = Employees.objects.all()
    return render(request,"employee.html",{'Emp':Emp})


# On Leave Employees Count and Page View : 

def onLeave(request):
    Emp = Employees.objects.all()
    di = {}
    for i in Emp:
        if i.Active == True:
            di[i] = Emp
    print(di)
    return render(request,'onLeaveEmployee.html',{'Emp':di})        


# Particular Employee Details View:

def EmployeeDetails(request,id):
    filteredData = Employees.objects.filter(id = id)
    emp = Employees.objects.get(id=id)
    if emp.Active == False:
        emp.leave_count += 1
        emp.save()
    return render(request,'employeeDetails.html',{'Details':filteredData,'emp':emp})
    


# def incrementCount(request):
#     if request.method == "POST":
        

# Edit Employee Page View:

def EditEmployee(request,id):
    data = Employees.objects.filter(id=id)   
    return render(request,"EditEmployee.html",{'Data':data})

# The Function Which Was used to Edit The Employee :

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

# The Function Which  Was used to Delete the Employee :

def deleteEmployee(request,id):
    data = Employees.objects.get(id= id)
    data.delete()
    print(data)
    return redirect('Employee')


# The Function Which Was used To Update The Active Status To True : 

def update_object(request, id):
    obj = get_object_or_404(Employees,id=id)
    obj.Active = True
    obj.save()
    return redirect('Employee')

# The Function Which Was used To Update The Active Status To False : 

def update_object1(request, id):
    obj = get_object_or_404(Employees,id=id)
    obj.Active = False
    obj.save()
    return redirect('Employee')



def reset_count(request, id):
    obj = get_object_or_404(Employees,id=id)
    obj.leave_count = 0
    obj.save()
    return redirect('Employee')
