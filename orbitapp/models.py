# myapp/models.py
from django.db import models

class Card(models.Model):
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    apply_link = models.URLField()
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Quote(models.Model):
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.text


