from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):

    user = models.OneToOneField(User)

    def __str__(self):
        return self.user