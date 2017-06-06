# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.

#---------------------------------------------
#   ShiftHandover Model
#---------------------------------------------

    #-----------------
    #   ShiftHandover Main
    #-----------------
class sht(models.Model):
    date = models.DateField(auto_now_add=True)

    PART_OF_THE_DAY = (
        ('NS', 'Night Shift'),
        ('MS', 'Morning Shift'),
    )

    pd = models.CharField(
        max_length=2,
        choices = PART_OF_THE_DAY,
        default='MS',
        verbose_name='Part of the day',
    )

    class Meta:
        ordering = ["date"]
        verbose_name = "ShiftHandover"
        verbose_name_plural = "ShiftHandovers"

    def __str__(self):
        return str(self.date) + ' for ' + self.pd

    def __unicode__(self):
        return str(self.date) + 'for' + self.pd

    #-----------------
    #   ShiftHandover Monitoring (oneToMany - sht)
    #-----------------

class sht_monitoring(models.Model):
    sht = models.ForeignKey('sht', related_name='Monitoring_Handover', on_delete=models.CASCADE)
    IM = models.CharField(max_length=7)
    costumer = models.CharField(max_length=50, blank=True, null=True)
    application = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300)

    class Meta:
        ordering = ["IM"]
        verbose_name = "Monitoring"
        verbose_name_plural = "Monitoring Handover"

    def __str__(self):
        return self.IM

    def __unicode__(self):
        return self.IM

    #-----------------
    #   ShiftHandover Incidents (oneToMany - sht)
    #-----------------

class sht_incidents(models.Model):
    sht = models.ForeignKey('sht', related_name='Incident_Handover', on_delete=models.CASCADE)
    IM = models.CharField(max_length=7)
    costumer = models.CharField(max_length=50, blank=True, null=True)
    application = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300)

    class Meta:
        ordering = ["IM"]
        verbose_name = "Incident"
        verbose_name_plural = "Incident Handover"

    def __str__(self):
        return self.IM

    def __unicode__(self):
        return self.IM

    #-----------------
    #   ShiftHandover Tasks (oneToMany - sht)
    #-----------------

class sht_tasks(models.Model):
    sht = models.ForeignKey('sht', related_name='Task_Handover', on_delete=models.CASCADE)
    CM = models.CharField(max_length=7)
    TM = models.CharField(max_length=7)
    costumer = models.CharField(max_length=50, blank=True, null=True)
    application = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ["CM"]
        verbose_name = "Task"
        verbose_name_plural = "Change Handover"

    def __str__(self):
        return self.TM

    def __unicode__(self):
        return self.TM

    #-----------------
    #   ShiftHandover Other (oneToMany - sht)
    #-----------------

class sht_other(models.Model):
    sht = models.ForeignKey('sht', related_name='Other_Handover', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    class Meta:
        ordering = ["name"]
        verbose_name = "Other"
        verbose_name_plural = "Other Information"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
