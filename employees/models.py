from django.db import models
from django.urls import reverse

class Employee(models.Model):

	emp_id=models.CharField(unique=True, max_length=50, null=True)
	fname =models.CharField(max_length=50)
	lname =models.CharField(max_length=50)
	midname =models.CharField(max_length=50)
	birthDate =models.DateField(auto_now=False, auto_now_add=False)
	startDateOfEmployment=models.DateField(auto_now=False, auto_now_add=False)
	email =models.EmailField(max_length=200)
	phone_number=models.PositiveIntegerField()
	officeAssignment=models.CharField(max_length=100)
	position =models.CharField(max_length=100)
	employmentStatus=models.CharField(max_length=100)
	monthly_rate=models.DecimalField(max_digits=10, decimal_places=2)
	address=models.CharField(max_length=100)

	def __str__(self):
		return self.lname + ', ' + self.fname

	def get_absolute_url(self):
		return reverse('EmployeeInfo')
	
