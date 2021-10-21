from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(max_length=2000, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
