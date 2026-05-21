import os
from pathlib import Path

# Base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-dev-key-tijuana-2026')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')

# Aplicaciones Instaladas
INSTALLED_APPS = [
    'jazzmin', # Panel de administración moderno (Debe ir antes de django.contrib.admin)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    # Librerías extra
    'rest_framework',
    'corsheaders',
    # Tu aplicación local
    'gestion_clientes.apps.GestionClientesConfig',
]

# Capas de seguridad y procesamiento (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

# Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Modelo de Usuario Personalizado
AUTH_USER_MODEL = 'gestion_clientes.Usuario'

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Regionalización (Configurado para Tijuana)
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Tijuana'
USE_I18N = True
USE_TZ = True

# Archivos Estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Archivos Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ALLOW_ALL_ORIGINS = True 

# Configuración de Correo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'it.leconsultores@gmail.com'
EMAIL_HOST_PASSWORD = 'mdqk talm tlwg mqpr'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ADMIN_EMAIL = 'it.leconsultores@gmail.com'

# ==============================================================================
# CONFIGURACIÓN DE JAZZMIN (MOVIMIENTO DE BOTÓN POR JAVASCRIPT DETONADO)
# ==============================================================================
JAZZMIN_SETTINGS = {
    "site_title": "Administración",
    "site_header": "Control Central",
    "site_brand": "Panel de Control",
    "welcome_sign": "Bienvenido Arturo",
    "copyright": "ITT Mechatronics",
    "search_model": ["gestion_clientes.Cliente"],
    
    # Inyectamos JS directo que reubica físicamente el botón al cargar el DOM
    "custom_html": """
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            // Buscamos el contenedor del botón Agregar y el contenedor del Buscador/Filtros
            var botonAgregar = document.querySelector('.object-tools');
            var zonaBuscador = document.querySelector('#changelist-search');
            
            if (botonAgregar && zonaBuscador) {
                // Modificamos sus estilos sobre la marcha para que no choquen
                botonAgregar.style.float = 'left';
                botonAgregar.style.display = 'inline-block';
                botonAgregar.style.margin = '0 0 0 15px';
                botonAgregar.style.position = 'relative';
                
                zonaBuscador.style.float = 'left';
                zonaBuscador.style.marginRight = '10px';
                
                // Movemos físicamente el botón justo después del buscador
                zonaBuscador.parentNode.insertBefore(botonAgregar, zonaBuscador.nextSibling);
                
                // Arreglamos la separación del bloque de acciones de abajo
                var bloqueAcciones = document.querySelector('.actions');
                if (bloqueAcciones) {
                    bloqueAcciones.style.clear = 'both';
                    bloqueAcciones.style.paddingTop = '15px';
                }
            }
        });
    </script>
    <style>
        /* Ajuste de emergencia en CSS por si tarda en responder el script */
        .object-tools { float: left !important; margin-left: 15px !important; }
        #changelist-search { float: left !important; }
    </style>
    """,
    
    "icons": {
        "auth.Group": "fas fa-users",
        "gestion_clientes.Usuario": "fas fa-user-shield",
        "gestion_clientes.Cliente": "fas fa-building",
        "gestion_clientes.Documento": "fas fa-file-alt",
        "gestion_clientes.EstadoDocumento": "fas fa-traffic-light",
        "gestion_clientes.TipoDocumento": "fas fa-folder",
        "gestion_clientes.ReporteGenerado": "fas fa-history",
    },
    
    "order_with_respect_to": ["gestion_clientes", "auth"],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_fixed": True,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}