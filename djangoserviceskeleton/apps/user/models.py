from django.db import models
from django.core.validators import EmailValidator, ValidationError
from apps.user.password import *


class User(models.Model):
    email = models.CharField(
        max_length=254,
        unique=True,
        validators=[EmailValidator()],
    )

    password = models.CharField(
        max_length=160,
    )

    def __unicode__(self):
        return self.email

    def validate_unique(self, exclude=None):
        if self.pk is None:
            queryset = User.objects.filter(email__iexact=self.email)
        else:
            queryset = User.objects.filter(email__iexact=self.email).exclude(pk=self.pk)
        if len(queryset) != 0:
            raise ValidationError('Email not unique')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = encrypt(self.password)
        elif identify(self.password) is False:
            self.password = encrypt(self.password)
        super(User, self).save(*args, **kwargs)