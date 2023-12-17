from django.urls import path
from .views import categorias, posts_por_categoria , lista_posts
from .views_api import ObtenerCategorias, ObtenerActualizarEliminarCategoria, ObtenerPosts, ObtenerActualizarEliminarPost

urlpatterns = [
    path('categorias/', categorias, name='categorias'),
    path('categoria/<int:categoria_id>/', posts_por_categoria, name='posts_por_categoria'),
    path('posts/', lista_posts, name='lista_posts'),



    path('api/categorias/', ObtenerCategorias.as_view(), name='obtener-crear-categorias'),
    path('api/categorias/<int:pk>/', ObtenerActualizarEliminarCategoria.as_view(), 
        name='obtener-actualizar-eliminar-categoria'),

    path('api/posts/', ObtenerPosts.as_view(), name='obtener-crear-posts'),
    path('api/posts/<int:pk>/', ObtenerActualizarEliminarPost.as_view(), 
        name='obtener-actualizar-eliminar-post'),
]
