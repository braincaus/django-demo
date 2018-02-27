# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class New(models.Model):
    owner = models.ForeignKey(User, on_delete="cascade" )
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
