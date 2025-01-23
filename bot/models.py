from django.db import models


class Sender(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    first_message = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
