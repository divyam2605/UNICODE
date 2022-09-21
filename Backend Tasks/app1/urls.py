
from django.urls import path
from . import views 

urlpatterns = [
    path('fun/<int:n1>/<int:n2>', views.index, name='request'),
]