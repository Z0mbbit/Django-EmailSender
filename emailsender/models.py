from django.db import models

# Create your models here.

class Email(models.Model):
    emailadress = models.EmailField()

    def __str__(self):
        return self.emailadress