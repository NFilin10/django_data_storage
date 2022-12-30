from django.urls import path
from . import views


urlpatterns = [
    path('', views.model_form_upload, name='file'),
    # path('file', views.model_form_upload, name="file"),
]