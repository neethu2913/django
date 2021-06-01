from django.shortcuts import render

# Create your views here.
def stude_registration(request):
    return render(request, "stud/reg.html")
def stud_login(request):
    return render(request, "stud/login.html")
def feedback(request):
    return render(request, "stud/feedback.html")

