# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.utils import encoding
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class personel(models.Model):

    Name = models.CharField(unique=True,max_length=50)
    Position = models.CharField(max_length=50,default='SOME STRING')

    def __str__(self):
        return self.Name

@python_2_unicode_compatible
class DTE(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    nn = models.IntegerField()
    work = models.CharField(max_length=200)
    ESN = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)
    rezult = models.CharField(max_length=10)
    executor = models.ForeignKey(personel)
    elapsed_time = models.CharField(max_length=5)
    note = models.CharField(max_length=200)
    def __str__(self):
        return str(self.created_date)



class DPRS(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    nn = models.CharField(max_length=10)
    work = models.CharField(max_length=200)
    ESN = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)
    rezult = models.CharField(max_length=10)
    executor = models.CharField(max_length=20)
    elapsed_time = models.CharField(max_length=5)
    note = models.CharField(max_length=200)


class OKS(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    nn = models.CharField(max_length=10)
    work = models.CharField(max_length=200)
    ESN = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)
    rezult = models.CharField(max_length=10)
    executor = models.CharField(max_length=20)
    elapsed_time = models.CharField(max_length=5)
    note = models.CharField(max_length=200)

class ES(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    nn = models.CharField(max_length=10)
    work = models.CharField(max_length=200)
    ESN = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)
    rezult = models.CharField(max_length=10)
    executor = models.CharField(max_length=20)
    elapsed_time = models.CharField(max_length=5)
    note = models.CharField(max_length=200)

class BUH(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    nn = models.CharField(max_length=10)
    work = models.CharField(max_length=200)
    ESN = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)
    rezult = models.CharField(max_length=10)
    executor = models.CharField(max_length=20)
    elapsed_time = models.CharField(max_length=5)
    note = models.CharField(max_length=200)

class OV(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    nn = models.CharField(max_length=10)
    work = models.CharField(max_length=200)
    ESN = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)
    rezult = models.CharField(max_length=10)
    executor = models.CharField(max_length=20)
    elapsed_time = models.CharField(max_length=5)
    note = models.CharField(max_length=200)

class OTL(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    nn = models.CharField(max_length=10)
    work = models.CharField(max_length=200)
    ESN = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)
    rezult = models.CharField(max_length=10)
    executor = models.CharField(max_length=20)
    elapsed_time = models.CharField(max_length=5)
    note = models.CharField(max_length=200)



class BTS(models.Model):
    ECP = models.CharField(max_length=10)
    UCN = models.CharField(max_length=10)
    adress = models.CharField(max_length=50)


class report(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    dte = DTE.nn

# Create your models here.
