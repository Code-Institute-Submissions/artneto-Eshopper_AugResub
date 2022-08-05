from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=254, null=True, blank=False)
    subject = models.CharField(max_length=250, null=False, default='Add subject here', unique=True)
    message = models.TextField(null=False, default='Add message here')

    def __str__(self):
        return self.email