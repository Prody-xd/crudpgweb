from django.shortcuts import render

# Create your views here.
def ejApi(request):
    return render(request, 'core/ejemplos-api.html')
