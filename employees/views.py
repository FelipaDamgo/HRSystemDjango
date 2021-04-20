from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm
from django.template.loader import get_template
from .utils import render_to_pdf
from django.http import HttpResponse


class UserRegisterView(generic.CreateView):
	form_class=UserCreationForm
	template_name='registration/register.html'
	success_url=reverse_lazy('login')


class EmployeeInfo(ListView):
	model= Employee
	template_name = 'EmployeeInfo.html'
	

#def EmployeeInfo(request):
#	model = Employee
#	all_employee= Employee.objects.all
#	return render(request, 'EmployeeInfo.html', {'all':all_employee})

class EmployeeDetail(DetailView):
	model = Employee
	template_name = 'EmployeeDetail.html'

class AddEmployee(CreateView):
	model = Employee
	form_class = EmployeeForm
	template_name = 'AddEmployee.html'
	#fields = '__all__'

class UpdateEmployee(UpdateView):
	model= Employee
	form_class = EmployeeForm
	template_name = 'UpdateEmployee.html'
	#fields = '__all__'

class DeleteEmployee(DeleteView):
	model= Employee
	template_name = 'DeleteEmployee.html'
	success_url = reverse_lazy('EmployeeInfo')

class SearchEmployee(ListView):
	model = Employee
	template_name = 'EmployeeInfo.html'

	def get_queryset(self):
		query= self.request.GET.get('q')
		return Employee.objects.filter(fname__icontains=query)  

def Forms(request):
	return render(request, 'Forms.html', {})

def SRmodal(request):
	return render(request, 'searchSR.html', {})

class SearchSR(ListView):
	model = Employee
	template_name = 'SROpen.html'

	def get_queryset(self):
		query= self.request.GET.get('q')
		return Employee.objects.filter(fname__icontains=query)  

class ServiceRecord(DetailView):
	model = Employee
	template_name = 'ServiceRecord.html'
	#def get(self, request, *args, **kwargs):
		#template_name = 'COE.html'

	#	pdf= render_to_pdf('ServiceRecord.html')
	#	return HttpResponse(pdf, content_type='application/pdf')

def COEModal(request):
	return render(request, 'COEModal.html', {})

class SearchCOE(ListView):
	model = Employee
	template_name = 'COEOpen.html'

	def get_queryset(self):
		query= self.request.GET.get('q')
		return Employee.objects.filter(fname__icontains=query)  

class COE(DetailView):
	model = Employee
	#def get(self, request, *args, **kwargs):
	template_name = 'COE.html'

		#pdf= render_to_pdf('COE.html')
		
		#return HttpResponse(pdf, content_type='application/pdf')

	
		


