from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

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

def model_form_upload(request):

    if request.method == 'POST':
        print(request.POST)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            print("valid")
            password = request.POST.get("text")
            print(password)
            data = form.cleaned_data
            field = str(data['document'])
            extension = field.split(".")[1]
            if extension == "jpg":
                obj.description = "photo"
            else:
                obj.description = "doc"
            # obj.field1 = request.user
            obj.save()
            return redirect('/')
    else:
        form = DocumentForm()

        # return redirect('/')
        return render(request, 'main/layout.html')