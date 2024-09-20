from django.shortcuts import render, get_object_or_404, redirect

from personas.models import Persona
from personas.templates.personas.forms import PersonaForm


# Create your views here.
def bienvenido(request):
    no_personas = Persona.objects.count()
    personas = (Persona.objects
                .all()
                .order_by('-id'))

    dic = {
        'no_personas': no_personas,
        'personas': personas
    }
    return render(request, 'bienvenido.html', dic)


def detalle_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    dic = {'persona': persona}
    return render(request, 'personas/detallePersona.html', dic)

# Con esto podemos crear un formulario a partir de los campos de la tabla relacionada
# PersonaForm = modelform_factory(Persona, exclude=[])
def nueva_persona(request):
    if request.method == 'POST':
        forma_persona = PersonaForm(request.POST)
        if forma_persona.is_valid():
            forma_persona.save()
            return redirect('index')
    else:
        forma_persona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'forma_persona': forma_persona})

def editar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        forma_persona = PersonaForm(request.POST, instance=persona)
        if forma_persona.is_valid():
            forma_persona.save()
            return redirect('index')
    else:
        forma_persona = PersonaForm(instance=persona)
    return render(request, 'personas/nuevo.html', {'forma_persona': forma_persona})

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')