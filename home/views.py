from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from home.models import Form
from home.models import Form1
from home.models import Form2
from home.models import Form3

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        stream = request.POST.get('stream')

        # Check if any of the fields are empty
        if not name or not age or not stream:
            return HttpResponse("Please fill in all the required fields")

        # If all fields are provided, save the data to the database
        ins = Form(name=name, age=age, stream=stream)
        ins.save()
        return HttpResponseRedirect("/redirect1/")

    return render(request, "Home.html")
def begin(request):
    return render(request,"begin.html")
def redirect1(request):
    if request.method == 'POST':
        # Assuming you want to retrieve the answers from the form
        answer1 = request.POST.get('t1', '')
        answer2 = request.POST.get('t2', '')
        answer3 = request.POST.get('t3', '')
        if not answer1 or not answer2 or not answer3:
            return HttpResponse("Please fill in all the required fields")
        print(answer1, answer2, answer3)
        
        # Save the answers to a Form1 model instance
        ins = Form1(answer1=answer1, answer2=answer2, answer3=answer3)
        ins.save()
        
        return HttpResponseRedirect("/redirect2/")

    return render(request, "redirect1.html")

def redirect2(request):
    if request.method == 'POST':
        # Assuming you want to retrieve the answers from the form
        answer4 = request.POST.get('t4', '')
        answer5 = request.POST.get('t5', '')
        answer6 = request.POST.get('t6', '')
        if not answer4 or not answer5 or not answer6:
            return HttpResponse("Please fill in all the required fields")
        print(answer4, answer5, answer6)
        
        # Save the answers to a Form1 model instance
        ins = Form2(answer4=answer4, answer5=answer5, answer6=answer6)
        ins.save()
        
        return HttpResponseRedirect("/redirect3/")

    return render(request, "redirect2.html")
def redirect3(request):
    return render(request,'redirect3.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        # Assuming you want to retrieve the answers from the form
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        message= request.POST.get('message', '')
        if not name or not email or not message:
            return HttpResponse("Please fill in all the required fields")
        print(name,email ,message )
        
        # Save the answers to a Form1 model instance
        ins = Form3(name=name, email=email, message=message)
        ins.save()
        
        return HttpResponseRedirect("/ThanksForContacting/")
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def ThanksForContacting(request):
    return render(request,'ThanksForContacting.html')

