from django.db import models

# Create your models here.
class signup(models.Model):
    companyname = models.CharField(max_length=40)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    website = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

class Detail(models.Model):
    aluminum = models.CharField(max_length=50)  # To store '12-18 metric tons'
    bauxite = models.CharField(max_length=50)
    alumina = models.CharField(max_length=50)
    causticsoda = models.CharField(max_length=50)
    lime = models.CharField(max_length=50)
    cryolite = models.CharField(max_length=50)
    carbonanodes = models.CharField(max_length=50)
    electricity = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
