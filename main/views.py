from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.contrib.auth.decorators import login_required


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

    if request.method == 'POST':
        print(request.FILES)

        for i in request.FILES.getlist('myFile'):
            print(i)
        # user_value = request.POST.get("myFile")
        # print(user_value)
        return redirect('/')
        # return redirect('/')
        # print(request.POST)
        # form = DocumentForm(request.POST, request.FILES)
        # if form.is_valid():
        #     obj = form.save(commit=False)
        #     print("valid")
        #     password = request.POST.get("text")
        #     print(password)
        #     obj.user = request.user
        #     obj.save()
        #     x = Document.objects.filter(user=request.user)
        #     print(x)
        #     return redirect('/')
        # else:
        #     print(form.errors)
        #     # return redirect('/')
    else:
       # form = DocumentForm()

        return render(request, 'main/layout.html')
