from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('', views.model_form_upload, name='file'),
    path('', login_required(views.model_form_upload), name='home'),
    path('all', login_required(views.all_files), name='all'),
    path('all/down/<file_id>', login_required(views.all_files1), name='down'),
    # path('file', views.model_form_upload, name="file"),
]