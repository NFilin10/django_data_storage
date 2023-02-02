from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('', views.model_form_upload, name='file'),
    path('', login_required(views.model_form_upload), name='home'),
    path('all_files', login_required(views.all_files), name='all_f'),
    path('all_notes', login_required(views.all_notes), name='all_n'),
    path('pictures', login_required(views.pictures), name='pictures'),
    path('files', login_required(views.files), name='files'),
    path('links', login_required(views.links), name='links'),
    path('notes', login_required(views.notes), name='notes'),
    path('all/down/<file_id>', login_required(views.all_files1), name='down'),
    # path('file', views.model_form_upload, name="file"),
]