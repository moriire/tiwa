from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from upload.views import UploadViews, ProductViews
router = DefaultRouter()
router.register("upload", UploadViews)
router.register("product", ProductViews)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/", include(router.urls))
]