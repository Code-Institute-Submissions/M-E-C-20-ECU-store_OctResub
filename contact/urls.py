from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('admin/', views.contact_admin, name='contact_admin'),
]
