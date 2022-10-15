from django.shortcuts import render

# Create your views here.
def indexevaluasi(request):
    return render(request, 'evaluasi.html')