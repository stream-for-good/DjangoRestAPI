from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'api/list_auth_messages', views.ListAuthTokenViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/encrypted_token", views.EncryptedTokenView.as_view(), name='encrypted_token'),
]