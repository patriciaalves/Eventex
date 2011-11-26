# -*- coding: utf-8 -*-
from django.db import models

class Subscription(models.Model):
  name= models.CharField(max_length = 100, verbose_name='Nome')
  cpf = models.CharField(max_length=11, unique = True, verbose_name='CPF')
  email = models.EmailField(unique=True, verbose_name='E-mail')
  phone= models.CharField(max_length=20, blank=True, verbose_name='Telefone')
  created_at = models.DateTimeField(auto_now_add = True)

  class Meta:
    ordering = ["created_at"]
    verbose_name = "Inscrição"
    verbose_name_plural = "Inscrições"

  def __unicode__(self):
    return self.name
