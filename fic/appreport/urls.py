from django.urls import path, include
from .import views

urlpatterns = [
    path('download_pdf/', views.generate_pdf_view, name='download_pdf'),
]