from django.urls import path
from . import views
from .views import UserRegisterView, EmployeeDetail, AddEmployee, UpdateEmployee, DeleteEmployee, EmployeeInfo, SearchEmployee, SearchSR, ServiceRecord, SearchCOE, COE
urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register'),
	#path('EmployeeInfo.html', views.EmployeeInfo, name='EmployeeInfo'),
	path('EmployeeInfo.html', EmployeeInfo.as_view(), name='EmployeeInfo'),
	path('Employee/<int:pk>', EmployeeDetail.as_view(), name='EmployeeDetail'),
	path('AddEmployee/', AddEmployee.as_view(), name='AddEmployee'),
	path('UpdateEmployee/<int:pk>', UpdateEmployee.as_view(), name='UpdateEmployee'),
	path('DeleteEmployee/<int:pk>', DeleteEmployee.as_view(), name='DeleteEmployee'),
	path('SearchEmployee/', SearchEmployee.as_view(), name='SearchEmployee'),
	path('Forms/', views.Forms, name='Forms'),
	path('SRModal/', views.SRmodal, name='SRmodal'),
	path('SearchSR/', SearchSR.as_view(), name='SearchSR'),
	path('ServiceRecord/<int:pk>', ServiceRecord.as_view(), name='ServiceRecord'),
	path('COEModal/', views.COEModal, name='COEModal'),
	path('SearchCOE/', SearchCOE.as_view(), name='SearchCOE'),
	path('COE/<int:pk>', COE.as_view(), name='COE'),
]
