from django.db import models

# Create your models here.
class data(models.Model):
	fname = models.CharField(max_length=250)
	lname = models.CharField(max_length=250)
	passo = models.CharField(max_length=250)
	stud = models.CharField(max_length=250)
	insti = models.CharField(max_length=250)
	phone = models.CharField(max_length=250)
	email = models.CharField(max_length=250)

class noti(models.Model):
	noti = models.CharField(max_length=250)