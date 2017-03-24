from django.db import models

class Person(models.Model):
    contact_name = models.CharField(max_length=30)
    contact_email = models.EmailField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.contact_name, self.contact_email)
