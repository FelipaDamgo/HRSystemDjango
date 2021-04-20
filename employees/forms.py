from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('emp_id','fname','lname','midname', 'birthDate', 'startDateOfEmployment', 'email', 'phone_number', 'officeAssignment', 'position', 'employmentStatus', 'monthly_rate','address',)
		widgets = {
			'emp_id':forms.TextInput(attrs={'class':'form-control'}),
			'fname':forms.TextInput(attrs={'class':'form-control'}),
			'lname':forms.TextInput(attrs={'class':'form-control'}),
			'midname':forms.TextInput(attrs={'class':'form-control'}),
			'birthDate':forms.TextInput(attrs={'class':'form-control'}),
			'startDateOfEmployment':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'phone_number':forms.TextInput(attrs={'class':'form-control'}),
			'officeAssignment':forms.TextInput(attrs={'class':'form-control'}),
			'position':forms.TextInput(attrs={'class':'form-control'}),
			'employmentStatus':forms.TextInput(attrs={'class':'form-control'}),
			'monthly_rate':forms.TextInput(attrs={'class':'form-control'}),
			'address':forms.TextInput(attrs={'class':'form-control'}),

		}

	