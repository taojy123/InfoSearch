# -*- coding: utf-8 -*-

from django.db import models


class Info(models.Model):
    uid = models.CharField(max_length=64, blank=True , null=True)
    key = models.CharField(max_length=64, blank=True , null=True)
    value = models.CharField(max_length=255, blank=True , null=True)

class Keys(models.Model):
    name = models.CharField(max_length=64, blank=True , null=True)

class Index(models.Model):
    uid = models.CharField(max_length=64, blank=True , null=True)

    def get_value(self, key):
        info = Info.objects.filter(uid=self.uid).filter(key=key)
        if info:
            return info[0].value
        else:
            return "-"




