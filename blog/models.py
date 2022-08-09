""" module for journal page"""
from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=250, null=False, default="",
                             unique=True)
    body = models.TextField(null=False, default="")
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.title
