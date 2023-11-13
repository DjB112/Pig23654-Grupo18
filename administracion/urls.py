from django.urls import path
from . import views as administracion_views

urlpatterns = [
    path('registrar/',administracion_views.registrar,name="registrar"),
    path('sesion/', administracion_views.sesion, name="sesion"),        
    path('busqueda/', administracion_views.busqueda,name="busqueda"),
    # Seccion Administracion
    path('',administracion_views.administracion, name="administracion"),
    # Seccion Novedades
    path('novedades/',administracion_views.NovedadListView.as_view(), name="novedad_index"),
    path('novedades/nueva',administracion_views.NovedadCreateView.as_view(), name="novedad_nueva"),
    path('novedad/editar/<int:pk>', administracion_views.NovedadUpdateView.as_view(), name="novedad_editar"),
    path('novedad/baja/<int:pk>', administracion_views.NovedadDeleteView.as_view(), name="novedad_baja"),
    # Seccion Personas
    path('persona/',administracion_views.PersonaListView.as_view(),name="persona_index"),
    path('persona/alta',administracion_views.PersonaCreateView.as_view(), name="persona_alta"),
    path('persona/modificacion/<int:pk>',administracion_views.PersonaUpdateView.as_view(), name="persona_modificacion"),
    path('persona/baja/<int:pk>', administracion_views.PersonaDeleteView.as_view(), name='persona_baja'),
    # Seccion Categorias
    path('categoriasproyecto/', administracion_views.CategoriasproyectoListView.as_view(),name="categoriasproyecto_index"),
    path('categoriasproyecto/nuevo/', administracion_views.CategoriasproyectoCreateView.as_view(),name="categoriasproyecto_nuevo"),
    path('categoriasproyecto/editar/<int:pk>', administracion_views.CategoriasproyectoUpdateView.as_view(),name="categoriasproyecto_editar"),
    path('categoriasproyecto/baja/<int:pk>', administracion_views.CategoriasproyectoDeleteView.as_view(),name="categoriasproyecto_baja"),
    path('categoriascolaboracion/', administracion_views.CategoriascolaboracionListView.as_view(),name="categoriascolaboracion_index"),
    path('categoriascolaboracion/nuevo/', administracion_views.CategoriascolaboracionCreateView.as_view(),name="categoriascolaboracion_nuevo"),
    path('categoriascolaboracion/editar/<int:pk>', administracion_views.CategoriascolaboracionUpdateView.as_view(),name="categoriascolaboracion_editar"),
    path('categoriascolaboracion/baja/<int:pk>', administracion_views.CategoriascolaboracionDeleteView.as_view(),name="categoriascolaboracion_baja"),
    # Seccion Proyectos
    path('proyectos/',administracion_views.ProyectoListView.as_view(),name="proyectos_index"),
    path('proyectos/nuevo/', administracion_views.ProyectoCreateView.as_view(),name="proyecto_alta"),
    path('proyectos/editar/<int:pk>',administracion_views.ProyectoUpdateView.as_view(),name="proyecto_editar"),
    path('proyectos/baja/<int:pk>',administracion_views.ProyectoDeleteView.as_view(),name="proyecto_baja"),
    path('proyectos/comentarios/<int:pk>',administracion_views.ComentarioProyectoListView.as_view(),name="comentarios_proyecto"),
    path('proyectos/comentario_editar/<int:pk>',administracion_views.ComentarioProyectoUpdateView.as_view(),name="comentario_editar"),
    path('proyectos/comentario_eliminar/<int:pk>',administracion_views.ComentarioProyectoDeleteView.as_view(),name="comentario_eliminar"),
    # Seccion Colaboracion
    path('colaboraciones/',administracion_views.ColaboracionListView.as_view(),name="colaboraciones_index"),
    path('colaboraciones/nuevo/', administracion_views.ColaboracionCreateView.as_view(),name="colaboracion_alta"),
    path('colaboraciones/editar/<int:pk>',administracion_views.ColaboracionUpdateView.as_view(),name="colaboracion_editar"),
    path('colaboraciones/baja/<int:pk>',administracion_views.ColaboracionDeleteView.as_view(),name="colaboracion_baja"), 
]