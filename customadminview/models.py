from django.db import models
from jsonfield import JSONField
from django.contrib import admin
from django import forms
# Create your models here.

class BackendTeam(models.Model):
    team_members = JSONField(default = [])
