from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_pg, name='home'),
    path('file', views.model_form_upload, name="file")
]