from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
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

    doc_type_data = request.GET
    doc_type_dict = doc_type_data.dict()

    if request.method == 'POST':
        print("THIS IS POST", request.POST)


        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():

            for f in request.FILES.getlist('document'):
                instance = Document(file_type=request.POST.get('file_type'), document=f, user=request.user)
                instance.save()

            # x = Document.objects.filter(user=request.user)
            # print(x)
            return redirect('/')
        else:
            print(form.errors)
            return redirect('/')
    else:
       form = DocumentForm()

    return render(request, 'main/layout.html')
