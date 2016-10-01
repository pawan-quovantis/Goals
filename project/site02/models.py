from django.db import models
from django.contrib.auth.models import User
import hashlib


class UserExtended(User):
    hashed_email = models.CharField(max_length=255)

    REQUIRED_FIELDS = ["email"]

    def __repr__(self):
        return self.hashed_email

    def save(self, *args, **kwargs):
        self.hashed_email = str(hashlib.sha256(self.email).hexdigest())
        super.save()


class Abc(models.Model):
    name = models.CharField(max_length=102)
    last_name = models.CharField(max_length=12)

