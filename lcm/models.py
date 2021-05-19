from django.db import models

# Create your models here.
class LCM(models.Model):
	inputs = models.CharField(max_length=300)
	finalresult = models.CharField(max_length=300)
	firstfact = models.CharField(max_length=250)
	secondfact = models.CharField(max_length=250)
	slug = models.CharField(max_length=300)
	lastmodified = models.DateTimeField()
	li = models.CharField(max_length=250)