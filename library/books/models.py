from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=250)
	subtitle = models.CharField(max_length=250)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	isbn = models.CharField(max_length=13)

	def __str__(self):
		return self.title
