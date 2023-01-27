from django.shortcuts import render, redirect
from .forms import DocumentForm, NoteForm
from .models import Document, Note
from django.contrib.auth.decorators import login_required
import json

# @login_required()
def main_pg(request):
    return render(request, 'main/layout.html')


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         # test = Document(description="File")
#         if form.is_valid():
#             # data = form.cleaned_data
#             # field = data['document']
#             # print(field)
#             form.save()
#         t = Document.objects.get(id=23)
#         t.description = 'test file'
#         t.save()
#
#     else:
#         form = DocumentForm()
#     return render(request, 'main/layout.html', {
#         'form': form
#     })
@login_required()
def model_form_upload(request):

    form = NoteForm(request.POST, request.FILES)

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

    return render(request, 'main/layout.html', {'form':form})
