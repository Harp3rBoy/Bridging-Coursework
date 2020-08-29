from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('personal_details/edit/', views.personal_details_edit, name='edit_personal_details'),
    path('education/new/', views.education_new, name='new_education')
]
