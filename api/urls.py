from django.urls import path

from api.views.group import add, remove
from api.views.login import TokenObtainPairView
from api.views.user import me

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/me/", me, name="me"),
    path("group/<str:name>/add/", add, name="add"),
    path("group/<str:name>/remove/", remove, name="remove"),
]
