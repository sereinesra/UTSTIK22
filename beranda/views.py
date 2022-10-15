from django.shortcuts import render

# Create your views here.
def indexberanda(request):
    return render(request, 'beranda.html')