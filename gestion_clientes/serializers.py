from rest_framework import serializers
from .models import (
    Cliente, Documento, TipoDocumento, 
    HistorialDocumento, EstadoDocumento, ConfiguracionAlerta
)

# =========================
# 1. SERIALIZER DE ESTADOS
# =========================
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoDocumento
        fields = '__all__'

# =========================
# 2. SERIALIZER DE DOCUMENTOS (EL PRINCIPAL)
# =========================
class DocumentoSerializer(serializers.ModelSerializer):
    # Campos calculados (ReadOnly) para que el frontend reciba nombres en lugar de IDs
    tipo_nombre = serializers.ReadOnlyField(source='tipo.nombre_tipo')
    
    # IMPORTANTE: Se cambió 'nombre_estado' a 'nombre' para coincidir con el modelo de Hugo
    estado_nombre = serializers.ReadOnlyField(source='estado.nombre') 
    
    color_estado = serializers.ReadOnlyField(source='estado.color')
    cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre')
    creado_por_nombre = serializers.ReadOnlyField(source='creado_por.username')

    class Meta:
        model = Documento
        fields = [
            'id_documento',   # Mapeado desde el primary key del modelo
            'cliente',        # ID para escritura
            'cliente_nombre', # Nombre para lectura
            'tipo',           # ID para escritura
            'tipo_nombre',    # Nombre para lectura
            'estado',         # ID para escritura
            'estado_nombre',  # Nombre para lectura
            'color_estado',
            'fecha_vencimiento',
            'fecha_detencion',
            'notas',
            'archivo',        # Manejado por el FileField configurado en settings
            'nombre_archivo',
            'tipo_mime',
            'tamano',
            'creado_por_nombre',
            'creado_en'
        ]

# =========================
# 3. SERIALIZER DE CLIENTES
# =========================
class ClienteListSerializer(serializers.ModelSerializer):
    # Muestra la lista de documentos de cada cliente
    # Nota: Requiere related_name='documentos' en el ForeignKey de Documento hacia Cliente
    documentos = DocumentoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = [
            'id_cliente', 
            'nombre', 
            'telefono', 
            'email', 
            'direccion', 
            'documentos'
        ]

# =========================
# 4. SERIALIZER DE HISTORIAL
# =========================
class HistorialSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='usuario.username')
    
    class Meta:
        model = HistorialDocumento
        fields = [
            'id_historial',
            'documento',
            'estado_anterior',
            'estado_nuevo',
            'fecha_cambio',
            'usuario_nombre',
            'comentario'
        ]

# =========================
# 5. SERIALIZER DE CONFIGURACIÓN
# =========================
class ConfiguracionAlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionAlerta
        fields = '__all__'