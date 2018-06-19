# -*- coding: utf-8 -*-
from datetime import datetime, date, time
from django.utils import timezone

from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Ads,Tags
from .forms import AdForm,FilterForm

def ads_list(request):

    ad = Ads.objects.order_by('created_date')



    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            #tegs=list((form.cleaned_data['tegs']).values())[0][u'id']
            Tegs=form.cleaned_data['tegs']

            activ=form.cleaned_data['activ']
            start_date = form.cleaned_data['start_date']
            stop_date = form.cleaned_data['stop_date']
            text_content = form.cleaned_data['text_content']
            ad = Ads.objects.filter(tegs=Tegs.values('id'),created_date__gte=start_date,created_date__lte=stop_date,text__contains=text_content)
            print(activ,start_date,stop_date,text_content)
            #ad.save()
            #form.save_m2m()
            return render(request, 'anonim/ads.html', {'form': form, 'ads': ad})
            #+str(tegs)+'/'+str(activ)+'/'+str(start_date)+'/'+str(stop_date)+'/'+str(text_content))

    else:
        form = FilterForm()


    return render(request, 'anonim/ads.html', {'form': form,'ads':ad})



def ads_filter(request,teg,activ,b_date,s_date,text):

    ad = Ads.objects.order_by('created_date').filter(teg=teg).filter(date__range=[b_date,s_date]).filter(text__contains=text)



    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.save()
            form.save_m2m()
            return redirect('ads_list')

    else:
        form = FilterForm()


    return render(request, 'anonim/ads.html', {'form': form,'ads':ad})


def new_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.save()
            form.save_m2m()
            return redirect('ads_list')

    else:
        form = AdForm()
    return render(request, 'anonim/new_ad.html', {'form': form})


# Create your views here.
