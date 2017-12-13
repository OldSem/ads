from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Max


# Create your views here.
from .forms import personelForm, DTEForm
from .models import DTE
    
def frame(request):
    return render(request,'parser/frame.html')


def dte_list(request):
    dtes = DTE.objects.order_by('created_date')
    return render(request, 'everyday/dtes.html', {'dtes': dtes})

def personel_new(request):
        if request.method == "POST":
                form = personelForm(request.POST)
                if form.is_valid():
                        personel = form.save(commit=False)

                        personel.save()

        else:
                form = personelForm()
        return render(request, 'everyday/personel_edit.html', {'form': form})


def dte_edit(request, nn):
        dte = get_object_or_404(DTE, nn=nn)
        if request.method == "POST":
                form = DTEForm(request.POST, instance=dte)
                if form.is_valid():
                        dte = form.save(commit=False)
                        dte.save()
                        return redirect('dte_list')
        else:
                form = DTEForm(instance=dte)
        return render(request, 'everyday/dte_edit.html', {'form': form})



def new_dte(request):

        if request.method == "POST":
                form = DTEForm(request.POST)
                if form.is_valid():
                        dte = form.save(commit=False)
                        dte.nn = DTE.objects.all().aggregate(Max('nn')).values[0] + 1
                        dte.save()
                        return redirect('dte_list')

        else:
                form = DTEForm()
        return render(request, 'everyday/new_dte.html', {'form': form})

def get_work(request):
        work_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['st']

        work_list = DTE.objects.filter(work__contains=starts_with).values('work','nn')
        wl=json.dumps(list(work_list), cls=DjangoJSONEncoder)
        #work_list = [entry for entry in work_list]
        #work_list = work_list[0]



        return HttpResponse(wl, content_type='application/json')