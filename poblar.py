import os
import django
import random
from datetime import date, timedelta

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from gestion_clientes.models import Cliente, TipoDocumento, EstadoDocumento, Documento

def poblar_sistema():
    print("Iniciando carga de datos para el ITT...")

    # 1. Crear Estados
    estados_data = [
        ('Vigente', 'verde'),
        ('Próximo a Vencer', 'amarillo'),
        ('Vencido', 'rojo'),
        ('No Aplica', 'gris')
    ]
    estados = {}
    for nombre, col in estados_data:
        obj, _ = EstadoDocumento.objects.get_or_create(nombre=nombre, color=col)
        estados[nombre] = obj

    # 2. Crear Tipos de Documentos
    tipos_nombres = ['Predial', 'Licencia de Operación', 'Certificado de Extintores', 'Uso de Suelo', 'Dictamen Eléctrico']
    tipos = {}
    for t in tipos_nombres:
        obj, _ = TipoDocumento.objects.get_or_create(nombre_tipo=t)
        tipos[t] = obj

    # 3. Datos de las 9 Empresas
    empresas_info = [
        ("Mobiliaria ITT", "664-123-4567", "contacto@m-itt.com", "Calzada Tecnológico 14433"),
        ("Vidrios Pepe", "664-987-6543", "ventas@vidriospepe.mx", "Blvd. Aguacaliente 1200"),
        ("Maquiladora Otay", "664-555-0101", "rh@maquilaotay.com", "Parque Industrial Otay"),
        ("Constructora Pacific", "664-444-2222", "proyectos@pacific.com", "Zona Río, Torre Norte"),
        ("Hotel Tijuana", "664-333-8888", "reservas@hoteltj.mx", "Av. Revolución 450"),
        ("Logística Aero", "664-222-9999", "envios@aero.com", "Aeropuerto Int. Tijuana"),
        ("Taller El Güero", "664-111-7777", "guero@taller.com", "Col. Libertad"),
        ("Café La Recta", "664-666-3333", "hola@larecta.cafe", "La Recta de la Cacho"),
        ("Farmacia Pacífico", "664-777-4444", "ayuda@farma-pacifico.com", "Playas de Tijuana")
    ]

    hoy = date.today()

    for nombre, tel, mail, dir in empresas_info:
        cliente, _ = Cliente.objects.get_or_create(
            nombre=nombre,
            defaults={'telefono': tel, 'email': mail, 'direccion': dir}
        )

        # Asignar 2 documentos por empresa con fechas variadas para ver todos los colores
        # Documento 1: Variado
        tipo1 = random.choice(list(tipos.values()))
        dias1 = random.choice([-5, 15, 60]) # Vencido, Próximo, Vigente
        vencimiento1 = hoy + timedelta(days=dias1)
        
        # Determinar estado según los días
        if dias1 < 0: est1 = estados['Vencido']
        elif dias1 < 30: est1 = estados['Próximo a Vencer']
        else: est1 = estados['Vigente']

        Documento.objects.create(
            cliente=cliente,
            tipo=tipo1,
            estado=est1,
            fecha_vencimiento=vencimiento1
        )

        # Documento 2: Otro tipo distinto
        tipo2 = random.choice([t for t in tipos.values() if t != tipo1])
        dias2 = random.choice([-10, 20, 120])
        vencimiento2 = hoy + timedelta(days=dias2)
        
        if dias2 < 0: est2 = estados['Vencido']
        elif dias2 < 30: est2 = estados['Próximo a Vencer']
        else: est2 = estados['Vigente']

        Documento.objects.create(
            cliente=cliente,
            tipo=tipo2,
            estado=est2,
            fecha_vencimiento=vencimiento2
        )

    print(f"¡Éxito! Se crearon 9 empresas y {Documento.objects.count()} documentos.")

if __name__ == '__main__':
    poblar_sistema()