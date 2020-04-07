from django.shortcuts import render
from .models import Contato
from django.core.paginator import Paginator

def index(request):

    contato = Contato.objects.all()

    paginator = Paginator(contato, 2)

    page = request.GET.get('p')
    contato = paginator.get_page(page)

    return render(request, 'contatos/index.html',{
                    'contatos': contato
                  })


def ver_contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)

    return render(request, 'contatos/ver_contato.html', {'contato': contato})