# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Exam(models.Model):
    class Meta(object):
	ordering = ['group_exam']
	verbose_name=u"Екзамен"
	verbose_name_plural=u"Екзамени"
    date_exam=models.DateTimeField(
	blank=False,
	verbose_name=u"Час екзамену",
	null=True)
    teacher=models.CharField(
	max_length=256,
	blank=False,
	verbose_name=u"Викладач")
    group_exam=models.CharField(
	max_length=256,
	blank=False,
	verbose_name=u"Група")
    subject=models.CharField(
	blank=False,
	max_length=256,
	verbose_name=u"Предмет")
    def __unicode__(self):
	return u"%s%s"%(self.subject, self.group_exam)