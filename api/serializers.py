from rest_framework.serializers import ModelSerializer, SlugRelatedField

from users.models import User


class UserSerializer(ModelSerializer):
    groups = SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = User
        exclude = [
            "id",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "user_permissions",
        ]
