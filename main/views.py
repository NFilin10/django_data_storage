from django.shortcuts import render

def main_pg(request):
    return render(request, 'main/layout.html')
