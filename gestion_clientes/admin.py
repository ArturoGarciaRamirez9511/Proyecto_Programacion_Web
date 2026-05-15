from django.contrib import admin
from .models import (
    Usuario, Cliente, Documento, TipoDocumento, 
    EstadoDocumento, ReporteGenerado
)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'rol', 'email')
    search_fields = ('username', 'nombre')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'email', 'telefono')
    search_fields = ('nombre',)

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_tipo')

@admin.register(EstadoDocumento)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'color')

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_documento', 'cliente', 'tipo', 'estado', 'fecha_vencimiento')
    list_filter = ('estado', 'tipo', 'cliente')

@admin.register(ReporteGenerado)
class ReporteAdmin(admin.ModelAdmin):
    # Mostramos los campos nuevos que agregamos para tu tabla
    list_display = ('id_reporte', 'cliente', 'tipo_tramite', 'estatus_doc', 'usuario_creador', 'fecha_creacion')
    readonly_fields = ('fecha_creacion',)
    list_filter = ('tipo_tramite', 'estatus_doc')