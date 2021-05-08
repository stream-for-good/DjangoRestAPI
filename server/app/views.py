import base64

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import AuthToken
from .serializers import AuthTokenSerializer

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP


class ListAuthTokenViewSet(viewsets.ModelViewSet):
    queryset = AuthToken.objects.all().order_by("creation_date")
    serializer_class = AuthTokenSerializer


class EncryptedTokenView(APIView):
    def get(self, request):
        recipient_key = RSA.importKey(
            open("static/id_rsa.pub", encoding="us-ascii").read()
        )
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        random_bytes = get_random_bytes(1)

        # Encrypt with the public RSA key
        random_bytes_encrypted = cipher_rsa.encrypt(random_bytes)

        # Save info
        token = AuthToken(
            clear_message=random_bytes, encrypted_message=random_bytes_encrypted
        )
        token.save()

        return Response(
            {
                "pk": token.pk,
                "encrypted_token": base64.b64encode(random_bytes_encrypted),
            },
            status=status.HTTP_200_OK,
        )
