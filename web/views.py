from django.shortcuts import render

from web.models import CV,Contact

# Create your views here.
def home(request):
    if request.method=='POST':
        user_name=request.POST.get('contactname')
        user_email=request.POST.get('contactemail')
        desc=request.POST.get('contactdesc')
       

        contact=Contact(name=user_name,contact_email=user_email,desc=desc)
        contact.save()
   

    return render(request,'home.html')
def thank(request):
    if request.method=='POST':
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        cvfile = request.FILES.get('cv')
      
        cv=CV(fullname=user_name,user_email=user_email,cv=cvfile)
        cv.save()


    return render(request,'thanks.html')