# -*- coding: utf-8 -*-
from django import forms
from subscriptions.models import Subscription

class SubscriptionForm(forms.ModelForm):
  name = forms.CharField(error_messages={'required': u'O campo Nome é de preenchimento obrigatório'}, label=u'Nome *')
  cpf = forms.CharField(error_messages={'required': u'O campo CPF é de preenchimento obrigatório'}, label=u'CPF *')
  email = forms.EmailField(error_messages={'required': u'O campo E-mail é de preenchimento obrigatório', 'invalid': 'Entre com um E-mail válido'}, label=u'E-mail *')
  class Meta:
    model = Subscription
    exclude = ('created_at')

