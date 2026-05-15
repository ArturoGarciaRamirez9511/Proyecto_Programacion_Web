from rest_framework import serializers
from .models import Usuario, Cliente, Documento, TipoDocumento, EstadoDocumento, ReporteGenerado

class DocumentoSerializer(serializers.ModelSerializer):
    tipo_nombre = serializers.ReadOnlyField(source='tipo.nombre_tipo')
    estado_nombre = serializers.ReadOnlyField(source='estado.nombre') 
    semaforo_dinamico = serializers.ReadOnlyField(source='semaforo_color')
    cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre')

    class Meta:
        model = Documento
        fields = '__all__'

class ClienteListSerializer(serializers.ModelSerializer):
    documentos = DocumentoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = '__all__'

class ReporteGeneradoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre')
    usuario_nombre = serializers.ReadOnlyField(source='usuario_creador.username')
    
    class Meta:
        model = ReporteGenerado
        fields = [
            'id_reporte', 'cliente', 'cliente_nombre', 'usuario_creador', 
            'usuario_nombre', 'tipo_tramite', 'estatus_doc', 
            'notas_reporte', 'fecha_creacion'
        ]

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoDocumento
        fields = '__all__'