from django.db import models

# Create your models here.




class employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class project(models.Model):
    status_choice=(
        ('blocked','blocked'),
        ('in_active','in_active'),
        ('in_progress','in_progress')
    )
    priority_choice=(
        ('low','low'),
        ('medium','medium'),
        ('high','high')
    )

    task=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=35,choices=status_choice,default='in_progress')
    priority=models.CharField(max_length=35,choices=priority_choice,default='medium')
    assigned_To=models.ForeignKey(employee,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
   
