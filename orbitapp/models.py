# myapp/models.py
from django.db import models

class Card(models.Model):
    company_name = models.CharField(max_length=100 )
    designation = models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Quote(models.Model):
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.text

class Senior(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    working_in = models.CharField(max_length=100)    


