from rest_framework_simplejwt import serializers, views


class TokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["groups"] = [name for name in user.groups.values_list("name", flat=True)]
        return token


class TokenObtainPairView(views.TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
