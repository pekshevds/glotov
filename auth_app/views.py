from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.models import Token


class TokenView(APIView):
    """
    Новый токен
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        token = Token.objects.create()
        if token:
            return Response({"data": {"token": token.id}})
        return Response({"data": None})
