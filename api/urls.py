from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from api.views.user import me

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/me/", me, name="me"),
]
