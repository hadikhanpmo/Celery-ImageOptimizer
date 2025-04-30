from django.urls import path
from . import views

app_name = 'image_processing'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('upload_success/', views.upload_success, name='upload_success'),
]
