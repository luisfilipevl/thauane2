from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from django.db.models.functions import Lower
from django.core.paginator import Paginator

# Create your views here.
@login_required
def inicio_gerencia(request):
    return render(request, 'gerencia/inicio.html')

def listagem_noticia(request):
    formularioFiltro = NoticiaFilterForm(request.GET or None)
    
    noticias = Noticia.objects.filter(usuario=request.user)  # Filtra pelo usuário logado

    if formularioFiltro.is_valid():
        if formularioFiltro.cleaned_data['titulo']:
            noticias = noticias.filter(titulo__icontains=formularioFiltro.cleaned_data['titulo'])
        if formularioFiltro.cleaned_data['data_publicacao_inicio']:
            noticias = noticias.filter(data_publicacao__gte=formularioFiltro.cleaned_data['data_publicacao_inicio'])
        if formularioFiltro.cleaned_data['data_publicacao_fim']:
            noticias = noticias.filter(data_publicacao__lte=formularioFiltro.cleaned_data['data_publicacao_fim'])
        if formularioFiltro.cleaned_data['Voo']:
            noticias = noticias.filter(Voo=formularioFiltro.cleaned_data['Voo'])
    
    contexto = {
        'noticias': noticias,
        'formularioFiltro': formularioFiltro
    }
    return render(request, 'gerencia/listagem_noticia.html',contexto)


def cadastrar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)  # Cria instância sem salvar
            noticia.usuario = request.user  # Atribui o autor (usuário logado)
            noticia.save()  # Salva a notícia no banco
            return redirect('gerencia:listagem_noticia')  # Redireciona para página de sucesso
    else:
        form = NoticiaForm() 

    contexto = {'form': form}
    return render(request, 'gerencia/cadastro_noticia.html', contexto)

@login_required
def editar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            noticia_editada = form.save(commit=False)  # Não salva ainda
            noticia_editada.usuario = request.user 
            noticia_editada.save()  # Salva com o usuário intacto
            return redirect('gerencia:listagem_noticia')
    else:
        form = NoticiaForm(instance=noticia)
    
    contexto = {
        'form': form
    }
    return render(request, 'gerencia/cadastro_noticia.html',contexto)




def index(request):
    Voo_nome = request.GET.get('Voo')  # Obtém o parâmetro 'Voo' da URL
    search_query = request.GET.get('search')  # Obtém o parâmetro de busca

    # Filtra as notícias com base na Voo ou na busca
    noticias = Noticia.objects.all()
    if Voo_nome:
        Voo = Voo.objects.filter(nome=Voo_nome).first()
        if Voo:
            noticias = noticias.filter(Voo=Voo)

    if search_query:
        noticias = noticias.filter(titulo__icontains=search_query)  # Filtra por título, ignorando maiúsculas/minúsculas

    Voos = Voo.objects.all()  # Pega todas as Voos para exibir no template

    contexto = {
        'noticias': noticias,
        'Voos': Voos,
        'Voo_selecionada': Voo_nome,
        'search_query': search_query,
    }
    return render(request, 'gerencia/index.html', contexto)





@login_required(login_url="usuarios:login")
def listagem_Voo(request):
    formularioFiltro = VooFilterForm(request.GET or None)
    voos = Voo.objects.all()  # Primeiro pega todos os voos
    if formularioFiltro.is_valid():
        if formularioFiltro.cleaned_data['nome']:
            # Aplique o filtro no queryset
            voos = voos.filter(nome__icontains=formularioFiltro.cleaned_data['nome'])

    voos = voos.order_by(Lower('nome'))  # Agora ordena os voos após o filtro
    paginator = Paginator(voos, 5)
    page = request.GET.get('page', 1)
    voos_paginados = paginator.page(page)  # Obtenha a página correta dos voos

    contexto = {
        'Voos': voos_paginados,
        'formularioFiltro': formularioFiltro
    }
    return render(request, 'gerencia/listagem_Voo.html', contexto)


@login_required(login_url="usuarios:login")
def cadastrar_Voo(request):
    if request.method == 'POST':
        form = VooForm(request.POST, request.FILES)
        if form.is_valid():
            Voo = form.save(commit=False)  
            Voo.save()  # Salva a Voo no banco
            return redirect('gerencia:listagem_Voo')  # Redireciona para página de sucesso
    else:
        form = VooForm() 

    contexto = {'form': form}
    return render(request, 'gerencia/cadastro_Voo.html', contexto)

@login_required(login_url="usuarios:login")
def editar_Voo(request, id):
    voo = Voo.objects.get(id=id)
    if request.method == 'POST':
        form = VooForm(request.POST, request.FILES, instance=Voo)
        if form.is_valid():
            Voo_editada = form.save(commit=False)  # Não salva ainda
            Voo_editada.usuario = request.user 
            Voo_editada.save()  # Salva com o usuário intacto
            return redirect('gerencia:listagem_Voo')
    else:
        form = VooForm(instance=voo)
    
    contexto = {
        'form': form
    }
    return render(request, 'gerencia/cadastro_Voo.html',contexto)

@login_required
def excluir_Voo(request, id):
    Voos = Voo.objects.get(id=id)
    Voos.delete()
    return redirect('gerencia:listagem_Voo')
