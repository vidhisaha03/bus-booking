from django.db import models



# Create your models here.
class TodoListItem(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField() 
    priority = models.TextField()
    shifts = models.TextField()
    passengers = models.TextField()
    Ac_type = models.TextField()
    date1=models.DateField(auto_now_add=True)
    




        
