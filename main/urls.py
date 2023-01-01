from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('', views.model_form_upload, name='file'),
    path('', login_required(views.model_form_upload), name='my_view'),
    # path('file', views.model_form_upload, name="file"),
]