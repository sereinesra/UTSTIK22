from django.shortcuts import render

# Create your views here.
def indexmateri(request):
    return render(request, 'materi.html')