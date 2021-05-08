from django.db import models


class AuthToken(models.Model):
    clear_message = models.BinaryField(null=False)
    encrypted_message = models.BinaryField(null=False)
    creation_date = models.DateTimeField(auto_now=True, null=False)
