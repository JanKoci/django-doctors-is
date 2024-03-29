from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient_list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('update/<int:pk>/', views.RegPatientUpdateView.as_view(), name='patient_update'),
    path('nr_update/<int:pk>/', views.NotRegPatientUpdateView.as_view(), name='notreg_patient_update'),
    path('nr_create/', views.NotRegisteredPatientCreateView.as_view(), name='notreg_patient_create'),
    path('create/', views.RegisteredPatientCreateView.as_view(), name='reg_patient_create'),
    path('delete/<int:pk>/', views.PatientDeleteView.as_view(), name='patient_delete'),
]
