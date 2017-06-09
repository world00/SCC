# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from dashboard.models import sht
from dashboard.forms import shtForm

#Create your views here.


class dashboardListView(ListView):
    model = sht

def show_sht(request):
    if request.method == "POST":
        form = shtForm(request.POST)
        if form.is_valid:
        #redirect to the url where you'll process the input
            return HttpResponseRedirect('sht_list.html') # insert reverse or url
        else:
            form = shtForm()
    return render(request, 'sht_list.html', {'form': form})
