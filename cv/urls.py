from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('personal_details/edit/', views.personal_details_edit, name='details_edit')
]
