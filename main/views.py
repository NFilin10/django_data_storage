from django.shortcuts import render, redirect
from .forms import DocumentForm, NoteForm
from .models import Document, Note
from django.contrib.auth.decorators import login_required
from random import shuffle
from django.http import FileResponse
import os
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper #django >1.8
from django.conf import settings


@login_required()
def main_page(request):
    last_5 = Document.objects.all().filter(user_id=request.user).order_by('-id')[:5]

    files_count = len(Document.objects.all().filter(user_id=request.user, file_type="Document"))
    pics_count = len(Document.objects.all().filter(user_id=request.user, file_type="Photo"))
    links_count = len(Note.objects.all().filter(user_id=request.user, file_type="Link"))
    notes_count = len(Note.objects.all().filter(user_id=request.user, file_type="Note"))


    if request.method == 'POST':
        print("THIS IS POST", request.POST)

        post_request = dict(request.POST)
        print(post_request['file_type'])
        if post_request['file_type'][0] == "Document" or post_request['file_type'][0] == "Photo":

            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                print("valid")
                for f in request.FILES.getlist('document'):
                    instance = Document(file_type=request.POST.get('file_type'), document=f, user=request.user)
                    instance.save()

                return redirect('/')
            else:
                print(form.errors)
                return redirect('/')

        elif post_request['file_type'][0] == "Link" or post_request['file_type'][0] == "Note":
            form = NoteForm(request.POST, request.FILES)
            if form.is_valid():
                print("second valid")
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect('/')
            else:
                print(form.errors)
                return redirect('/')
    else:
       form = DocumentForm()

    return render(request, 'main/home.html', {"recent":last_5, "files": files_count, "photos": pics_count, "links":links_count, "notes":notes_count})


def all_files(request):
    all_files = Document.objects.all().filter(user_id=request.user)


    return render(request, 'main/all_files.html', {"files":all_files})




def file_download(request, file_id):
    obj = Document.objects.filter(id=file_id, user_id=request.user.id).first()
    if obj:
        file_path = os.path.join(settings.MEDIA_ROOT, obj.document.name)
        filename = os.path.basename(file_path)
        chunk_size = 8192
        response = StreamingHttpResponse(
            FileWrapper(open(file_path, 'rb'), chunk_size),
            content_type="application/octet-stream"
        )
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        print(request.user.id, file_id)
        return redirect('/')


def all_notes(request):
    notes_obj = Note.objects.all().filter(user_id=request.user)
    return render(request, 'main/all_notes.html', {"notes":notes_obj})


def pictures(request):
    all_pictures = Document.objects.all().filter(user_id=request.user, file_type="Photo")
    return render(request, 'main/all_files.html', {"files": all_pictures})


def files(request):
    all_files = Document.objects.all().filter(user_id=request.user, file_type="Document")
    return render(request, 'main/all_files.html', {"files": all_files})


def links(request):
    links_obj = Note.objects.all().filter(user_id=request.user, file_type="Link")
    return render(request, 'main/all_notes.html', {"notes":links_obj})


def notes(request):
    note_obj = Note.objects.all().filter(user_id=request.user, file_type="Note")
    return render(request, 'main/all_notes.html', {"notes":note_obj})


def all_notes_delete(request, note_id):
    note_obj = Note.objects.filter(id=note_id)
    note_obj.delete()
    return redirect('all_n')

def notes_delete(request, note_id):
    note_obj = Note.objects.filter(id=note_id)
    note_obj.delete()
    return redirect('notes')