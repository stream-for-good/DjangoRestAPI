from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"authmessages", views.AuthMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
