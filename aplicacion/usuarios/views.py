from django.shortcuts import render
from .models import persona 

# Create your views here.
def mi_vista(request):
    clienteslistados = persona.objects.all()
    return render(request, 'gestionClientes.html',{'personas':clienteslistados})

