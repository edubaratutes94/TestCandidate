from django.db import models
from TestApp.utils import *
# Create your models here.

class Technology (models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name

class Candidates (models.Model):
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    name = models.CharField(max_length=255, verbose_name="Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    ci = models.CharField(verbose_name="ID", unique=True, max_length=11, validators=[validate_carne])
    address = models.CharField(verbose_name="Address", max_length=255)
    age = models.IntegerField(validators=[validate_only_numbers], verbose_name="Age")
    sex = models.CharField(max_length=250, verbose_name="Sex")

    def __str__(self):
        return self.name

class TechnologyCandidate (models.Model):
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    year = models.IntegerField(verbose_name="Years of experience", validators=[validate_only_numbers])
    technology = models.ForeignKey(Technology, verbose_name="Technology", on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidates, verbose_name="Candidate", on_delete=models.CASCADE)

    def __str__(self):
        return self.candidate.name
