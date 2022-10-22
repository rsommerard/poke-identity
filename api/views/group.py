import httpx
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add(request, name):
    response = httpx.get("https://pokeapi.co/api/v2/type")

    json = response.json()
    types = [result["name"] for result in json["results"]]

    if name not in types:
        return Response(status=status.HTTP_404_NOT_FOUND)

    group, _ = Group.objects.get_or_create(name=name)

    request.user.groups.add(group)

    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove(request, name):
    try:
        group = Group.objects.get(name=name)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    request.user.groups.remove(group)

    return Response(status=status.HTTP_200_OK)
