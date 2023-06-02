from django.db import models

# Create your models here.

class contactDetail(models.Model):
    fullname = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.fullname
    

class Register(models.Model):
    name = models.CharField(max_length=200, blank=True)
    phone_no = models.IntegerField("Phone Number")
    email = models.EmailField("Email")
    password = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.name} -> {self.email}"
    
class BioData(models.Model):
    height = models.IntegerField("Height")
    weight = models.IntegerField("Weight")
    age = models.IntegerField("Age")
    gender = models.CharField("Gender", max_length=10)
    vegetarian = models.BooleanField("Is Vegetarian")
    activity_level = models.CharField("Activity Level", max_length=50)
    body_goal = models.CharField("Body Goal",max_length=50)

    def __str__(self) -> str:
        return f"{self.height} {self.weight}"