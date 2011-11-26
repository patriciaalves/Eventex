# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import SubscriptionForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, resolve
from models import Subscription
from django.core.mail import send_mail
from django.conf import settings


def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)

    subscription = form.save()

    send_mail(subject=u'Cadastrado com Sucesso',
              message=u'Obrigado pela sua inscrição!',
              from_email=settings.DEFAULT_FROM_EMAIL,
              recipient_list=[subscription.email])

    return HttpResponseRedirect(
        reverse('subscriptions:success', args=[ subscription.pk ]))

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)
