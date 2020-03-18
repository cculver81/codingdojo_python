from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index)#,
    # path('some_function', views.some_function)
]