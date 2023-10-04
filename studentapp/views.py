import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import data

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_details(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        age = request.POST['age']
        dob = request.POST['dob']

        # Use request.POST.get() to get the selected gender with a default value of ''
        gender = request.POST.get('gender', '')

        qualifications = request.POST['qualifications']
        image = request.FILES.get('file')
        



        # Now you can use the 'gender' variable as needed
        if gender == 'male':
            # Handle the case where the gender is male
            # For example, you can print a message or perform specific actions
            print("Male selected")

        elif gender == 'female':
            # Handle the case where the gender is female
            # For example, you can print a message or perform specific actions
            print("Female selected")

        else:
            # Handle other cases or validation logic for gender
            # For example, you can show an error message or take appropriate actions
            print("Invalid gender selected")

        # Create and save the 'data' object
        data_ = data(firstname=fname, lastname=lname, age=age, dob=dob, gender=gender, qualifications=qualifications, image=image)
        data_.save()
        return redirect('student_showpage')
    

def student_showpage(request):
    showproducts=data.objects.all()
    return render(request,'Show.html',{'register':showproducts})

def product_editpage(request,pk):
    pr=data.objects.get(id=pk)
    return render(request,'edit.html',{'register':pr})


def edit_product_details(request, pk):
    # Get the existing data object to edit
    pr = get_object_or_404(data, id=pk)

    if request.method == 'POST':
        pr.firstname = request.POST.get('firstname')
        pr.lastname = request.POST.get('lastname')
        pr.age = float(request.POST.get('age'))
        pr.dob = request.POST.get('dob')

        # Use request.POST.get() to get the selected gender with a default value of ''
        gender = request.POST.get('gender', '')

        # Now you can use the 'gender' variable as needed
        if gender == 'male':
            # Handle the case where the gender is male
            # For example, you can print a message or perform specific actions
            print("Male selected")
            pr.gender = 'male'
        elif gender == 'female':
            # Handle the case where the gender is female
            # For example, you can print a message or perform specific actions
            print("Female selected")
            pr.gender = 'female'
        else:
            # Handle other cases or validation logic for gender
            # For example, you can show an error message or take appropriate actions
            print("Invalid gender selected")
            pr.gender = None

        pr.qualifications = request.POST.get('qualifications')
        old=pr.image
        new=request.FILES.get('file')
        if old!=None and new==None:
            pr.image=old
        else:
            pr.image=new
        #pr.image = request.FILES.get('file')
        pr.save()
        return redirect('student_showpage')

    return render(request, 'edit.html', {'register': pr})

def deletepage(request,pk):
    Productdetails=data.objects.get(id=pk)
    Productdetails.delete()
    return redirect ('student_showpage')
