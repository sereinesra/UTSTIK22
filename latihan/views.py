from django.shortcuts import render

# Create your views here.
def indexlatihan(request):
    return render(request, 'latihan.html')