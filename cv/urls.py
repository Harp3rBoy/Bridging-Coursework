from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('edit_post/', views.details_edit, name='details_edit')
]
