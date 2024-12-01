from django.shortcuts import render,redirect,HttpResponse
from todoapp.models import Todotask
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request,"index.html")
def save(request):
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        c_status=request.POST.get('c_status')
        obj=Todotask(title=title,description=description,completedstatus=c_status)
        obj.save()
        return redirect(home)

def display_task(request):
    data=Todotask.objects.all()
    return render(request,"task.html",{'data':data})

def update_task(request,uid):
    data=Todotask.objects.get(Tid=uid)
    return render(request,"update.html",{'data':data})

def update_save_task(request,uid):
    if request.method=="POST":
        description=request.POST.get('description')
        c_status=request.POST.get('c_status')
        # Get the task object
        obj = Todotask.objects.get(Tid=uid)
        # Update the task attributes(obj.modelsfield=variable)
        obj.description = description
        obj.completedstatus = c_status
        # Set the updated_at field to the current time
        obj.updated_at = timezone.now()
        # Save the changes to the task
        obj.save()
        return redirect(display_task)
    
def delete_todo(request,did):
    Todotask.objects.filter(Tid=did).delete()
    return redirect(display_task)
