from django.shortcuts import render

# Create your views here.
def archivo(request):
    data_context = {
        'nombre' : 'Luis Pardo',
        'edad' : 24,
        'pais' : 'Perú'
    }
    return  render(request, 'archivo.html', context={'data' : data_context})