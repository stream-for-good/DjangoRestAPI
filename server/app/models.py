from django.db import models


class AuthMessage(models.Model):
    clear_message = models.CharField(max_length=120, null=False)
    encrypted_message = models.CharField(max_length=120, null=False)
    creation_date = models.DateTimeField(auto_now=True, null=False)
