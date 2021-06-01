from django.shortcuts import render,redirect
from .forms import Todocreateform,TodoUpdateForm,UserRegistrationForm,Loginform
from .models import Todo
from django.contrib.auth import authenticate,login,logout

def login_required(func):
    def wrapper(request,id=None):
        if not request.user.is_authenticated:
            return redirect("loginview")
        else:
            return func(request,id)
    return wrapper

def create_todo(request,*args,**kwargs):
    if request.user.is_authenticated:
      context={}
      form=Todocreateform(initial={"user":request.user})
      context["form"]=form
      if request.method=="POST":
         form=Todocreateform(request.POST)
         if form.is_valid():
            task_name=form.cleaned_data.get("task_name")
            status=form.cleaned_data.get("status")
            user=form.cleaned_data.get("user")
            todo=Todo(task_name=task_name,status=status,user=user)
            todo.save()
            print("saved")
         return redirect("listall")
      return render(request,"todoapp/createtodo.html",context)
    else:
        return redirect("loginview")

@login_required
def list_all_todo(request,*args,**kwargs):
       todos=Todo.objects.filter(user=request.user)
       context={}
       context["todo"]=todos
       return render(request,"todoapp/listalltodo.html",context)


@login_required
def delete_todo(request,*args,**kwargs):
    id=kwargs.get("id")
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect("listall")

@login_required
def update_todo(request,*args,**kwargs):
    id = kwargs.get("id")
    todo=Todo.objects.get(id=id)
    form=TodoUpdateForm(instance=todo)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TodoUpdateForm(instance=todo,data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("listall")
    return render(request,"todoapp/edittodo.html",context)

def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginview")
        else:
            context["form"]=form
            return render(request, "todoapp/registration.html", context)
    return render(request,"todoapp/registration.html",context)

def django_login(request):
     form=Loginform()
     context={}
     context["form"]=form
     if request.method=="POST":
         form=Loginform(request.POST)
         if form.is_valid():
             username=form.cleaned_data.get("username")
             password=form.cleaned_data.get("password")
             user=authenticate(request,username=username,password=password)
             if user:
                 login(request,user)
                 return render(request,"todoapp/home.html")
             else:
                 context["form"]=form
         return render(request,"todoapp/login.html",context)
     return render(request,"todoapp/login.html",context)

def django_logout(request):
    logout(request)
    return redirect("loginview")