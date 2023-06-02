from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
def viewNote(request):
   try:
      not_completed = Note.objects.filter(isCompleted=False)
      print(not_completed)
      completed = Note.objects.filter(isCompleted=True)
      if request.method == "POST":
         try:
            task = request.POST.get('task')
            change = Note.objects.all()
            change.create(task=task)
            print(task)
         
         except:
            print("can't delete note")
   except:
      print("SOme Error")
   return render(request, 'core/index.html', {"not_completed": not_completed, "completed": completed})
   
  

def completeNote(request):
   print("Ok")
   try:
       if request.method == "GET":
         com_task = request.GET.get('task_id')
         change = Note.objects.filter(id=com_task)
         change.update(isCompleted=True)
         print(com_task)
         
   except:
      print("can't delete note")
   return redirect(viewNote)

def deleteNote(request):
   print("Ok")
   try:
       if request.method == "GET":
         del_task = request.GET.get('task_id')
         Note.objects.filter(id=del_task).delete()
         print("Done")

         
   except:
      print("can't delete note")
   return redirect(viewNote)   


def updateTask(request):
   try:
      if request.method == 'GET':
         id = request.GET.get('id')
         task = request.GET.get('task')
         change = Note.objects.filter(id=id)
         change.update(task=task)
   except:
      print("SOme error")
   return redirect(viewNote)

def uncompleteNote(request):
   print("Ok")
   try:
       if request.method == "GET":
         com_task = request.GET.get('task_id')
         change = Note.objects.filter(id=com_task)
         change.update(isCompleted=False)
         print(com_task)
         
   except:
      print("can't delete note")
   return redirect(viewNote)

