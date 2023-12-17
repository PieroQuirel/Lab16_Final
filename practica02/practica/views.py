from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Post

def posts_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = categoria.post_set.all()
    return render(request, 'posts_por_categoria.html', {'categoria': categoria, 'posts': posts})

def lista_posts(request):
    categoria_filtro = request.GET.get('categoria', '')

    if categoria_filtro:
        posts = Post.objects.filter(categoria__id=categoria_filtro)
    else:
        posts = Post.objects.all()

    categorias = Categoria.objects.all()

    return render(request, 'lista_posts.html', {'posts': posts, 'categorias': categorias})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})