from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('admin/', views.contact_admin, name='contact_admin'),
    path('admin/contact_message/<contact_id>',
         views.contact_message, name='contact_message'),
    path('delete/<int:contact_id>/',
         views.delete_contact, name='delete_contact'),
]
