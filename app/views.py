from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.shortcuts import render, get_object_or_404


from app.models import Usuario


# Create your views here.

def app(request):
    usuario = Usuario.objects.all()

    dados = {
        'usuarios': usuario
    }

    pagina = loader.get_template('home.html')
    return HttpResponse(pagina.render(dados))


def cadastro(request):
    return render(request, 'cadastro.html')


def cadastro_sucesso(request):
    return render(request, 'cadastro_sucesso.html')


def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('usuario')
        email = request.POST.get('email')
        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('cadastro_sucesso')
    else:
        return render(request, 'cadastro.html')
    
def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('app')

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        usuario.nome = nome
        usuario.email = email
        usuario.save()
        return redirect('app') 
    else:
        return render(request, 'app', {'usuario': usuario})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'base.html', {'usuarios': usuarios})
