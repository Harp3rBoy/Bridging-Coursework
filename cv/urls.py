from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('personal_details/edit/', views.personal_details_edit, name='edit_personal_details'),
    path('education/new/', views.education_new, name='new_education'),
    path('education/<pk>/edit', views.education_edit, name='edit_education'),
    path('education/<pk>/remove', views.education_remove, name='remove_education'),
    path('work_experience/new/', views.work_experience_new, name='new_work_experience'),
    path('work_experience/<pk>/edit', views.work_experience_edit, name='edit_work_experience'),
    path('work_experience/<pk>/remove', views.work_experience_remove, name='remove_work_experience'),
]
