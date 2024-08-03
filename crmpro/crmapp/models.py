from django.db import models

# Create your models here.

class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=200)

    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)

    def __str__(self):
        return(f"Name:{self.first_name} {self.last_name} email: {self.email}")
