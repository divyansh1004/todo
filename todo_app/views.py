from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.http import HttpResponse
from .models import todoview

# Create your views here.
#def todo(request):
  #  return render(request,'todolist.html')
def todoappview(request):
    item=todoview.objects.all()
    return render(request,'todolist.html',
     {'all_item':item})
def addtodoitem(request):
    x=request.POST['content']
    new_item=todoview(content=x)
    new_item.save()
    return HttpResponseRedirect('/todo_app/')
def deletetodoitem(request,i):
    y=todoview.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todo_app/')