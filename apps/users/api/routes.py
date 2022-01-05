from django.urls import path
from rest_framework.routers import SimpleRouter
from django_rest_passwordreset.urls import add_reset_password_urls_to_router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#custom views
from .views import RegisterView

router = SimpleRouter()
add_reset_password_urls_to_router(router, base_path='auth/passwordreset')

urls = []
urls = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls


