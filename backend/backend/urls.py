from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static
from upload.views import UploadViews, ProductViews, CategoryViews
from dj_rest_auth.registration.views import RegisterView
from user.models import CustomRegisterSerializer
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
#from rest_framework.schemas import get_schema_view

from rest_framework.documentation import include_docs_urls

# Swagger documentation setup
schema_view = get_schema_view(                        
                openapi.Info(
                title="Tiwa n Tiwa API Snippets",
                default_version='v1.0.1',
                description="Tiwa n Tiwa - Promoting African Cultural practices",
                website="/",
                terms_of_service="/terms_of_services/",
                privacy_policy="/privacy_policy/",
                contact=openapi.Contact(email="ibmabdulsalam@gmail.com",
                    phone = "+2348100482341"),                                           
                license = openapi.License(name="MIT License"),                                                    ),                                                public=True,
    permission_classes=[permissions.AllowAny],
)

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    
router = DefaultRouter()
router.register("category", CategoryViews)
router.register("upload", UploadViews)
router.register("product", ProductViews)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/register/", CustomRegisterView.as_view(), name="reg"),# include("dj_rest_auth.registration.urls")),
    path("api/", include(router.urls)),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)