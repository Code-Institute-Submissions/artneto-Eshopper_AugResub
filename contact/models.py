from django.db import models


class Contact(models.Model):
    email = models.EmailField(blank=True, default="")
    subject = models.CharField(max_length=255)
    message = models.TextField(null=False, default="")

    def __str__(self):
        return self.email