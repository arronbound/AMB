# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class PersonWhoSignedUp(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

# Create your models here.
