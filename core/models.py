from django.db import models

# Create your models here.
class Note(models.Model):
#    task_id = models.AutoField(primary_key=True)
   task = models.CharField(max_length=100)
   isCompleted = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.task 
    
   