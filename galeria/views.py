from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from galeria.models import Fotografia

def index(request):
    if not request.user.is_authenticated:   
        messages.error(request, 'Faça Login antes de acessar Home!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards':fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia':fotografia})
 
def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça Login antes de buscar!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    
    return render(request, 'galeria/buscar.html', {'cards':fotografias})

def categoria(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if ('nebulosa_bool' in request.GET and 
        request.GET['nebulosa_bool'] == 'true'):
        fotografias = fotografias.filter(categoria='NEBULOSA')

    elif ('estrela_bool' in request.GET and
        request.GET['estrela_bool'] == 'true'):
        fotografias = fotografias.filter(categoria='ESTRELA')

    elif ('galaxia_bool' in request.GET and
        request.GET['galaxia_bool'] == 'true'):
        fotografias = fotografias.filter(categoria='GALÁXIA')

    elif ('planeta_bool' in request.GET and
        request.GET['planeta_bool'] == 'true'):
        fotografias = fotografias.filter(categoria='PLANETA')         

    return render(request, 'galeria/categoria.html', {'cards':fotografias})