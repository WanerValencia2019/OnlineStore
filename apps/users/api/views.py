from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# jwt - AUTH
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# custom serializers
from .serializers import RegisterSerializer
from ...utils import get_tokens_for_user


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print()
        data = serializer.data
        del data["password"]

        token = get_tokens_for_user(user)

        return Response({"data": {"user": data, "token": token}}, status.HTTP_201_CREATED)
