from django.shortcuts import render

# Create your views here.
def indexrangkuman(request):
    return render(request, 'rangkuman.html')