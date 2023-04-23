
from djongo import models

class Employee(models.Model):
   
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    # created_at = models.DateTimeField(auto_now_add=True)
