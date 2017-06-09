# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import sht, sht_incidents, sht_monitoring, sht_tasks, sht_other, oncall

# Register your models here.

class sht_incidents_Inline(admin.StackedInline):
    model = sht_incidents
    extra = 1

class sht_monitoring_Inline(admin.StackedInline):
    model = sht_monitoring
    extra = 1

class sht_tasks_Inline(admin.StackedInline):
    model = sht_tasks
    extra = 1

class sht_other_Inline(admin.StackedInline):
    model = sht_other
    extra = 1

class shtAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Shift Handover for', {'fields': ['pd']}),
    ]
    inlines = [sht_incidents_Inline, sht_monitoring_Inline, sht_tasks_Inline, sht_other_Inline]

admin.site.register(oncall)

admin.site.register(sht, shtAdmin)