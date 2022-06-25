from django.db import models


class Newsletter(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.email