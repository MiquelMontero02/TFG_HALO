from django.template import loader
from django.http import HttpResponse

def forms(request):
    template=loader.get_template('Formulario.html')
    return HttpResponse(template.render())
