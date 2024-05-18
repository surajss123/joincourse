from django.db import models

# Create your models here.
class condact_info(models.Model):
    Name = models.CharField(max_length=50)
    Condact_Number = models.IntegerField(max_length=12)
    Email_id = models.EmailField(max_length=50)
    City = models.CharField(max_length=50)
    Course_Details = models.CharField(max_length=100)