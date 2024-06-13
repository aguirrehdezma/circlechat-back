from django.urls import path
from . import views

urlpatterns = [
    path('get_user_info/', views.get_user_info, name="get_user_info"),
]
