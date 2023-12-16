from django.shortcuts import render

# Create your views here.
def archivo_pokemon(request):
    data_context = {
        'nombre' : 'Squirtle',
        'numero' : '0007',
        'generacion' : 'primera',
        'tipo' : 'agua'
    }
    return render(request, template_name='archivo_p.html',context={'data' : data_context})


