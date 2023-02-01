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
def model_form_upload(request):
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

                # x = Document.objects.filter(user=request.user)
                # print(x)
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

    return render(request, 'main/layout.html', {"recent":last_5, "files": files_count, "photos": pics_count, "links":links_count, "notes":notes_count})



from django.http import HttpResponse

def all_files(request):
    all_files = Document.objects.all().filter(user_id=request.user)


    return render(request, 'main/all_files.html', {"files":all_files, "file_size":all_files})




def all_files1(request, file_id):
    print(file_id)
    obj = Document.objects.get(id=file_id)
    if request.user.id == file_id:
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
        return redirect('/')



    # return render(request, 'main/all_files.html', {'resp':response})