from django.http import HttpResponse
from .models import Paciente

def index(request):
    paciente_lista = Paciente.objects.order_by('paciente_apellido_text')[:5]
    output = ', '.join([p.paciente_apellido_text for p in paciente_lista])
    return HttpResponse(output)
