from django.shortcuts import render

# Create your views here.
def archivo_cat(request):
    data_context = {
        'nombre' : 'Charmander',
        'tipo' : 'Fuego',
        'habilidad' : 'mar fuego'
    }
    return render(request,'archivo_cat.html', context={'data' : data_context})

