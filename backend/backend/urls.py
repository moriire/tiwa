from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from upload.views import UploadViews, ProductViews
from dj_rest_auth.registration.views import RegisterView
from user.models import CustomRegisterSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

router = DefaultRouter()
router.register("upload", UploadViews)
router.register("product", ProductViews)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    #path("auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/", include(router.urls)),
    path('auth/register/', CustomRegisterView.as_view(), name='custom-register'),
]