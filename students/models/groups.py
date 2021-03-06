# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Group(models.Model):
    class Meta(object):
	ordering = ['title']
	verbose_name=u"Група"
	verbose_name_plural=u"Групи"
    title=models.CharField(
	max_length=256,
	blank=True,
	verbose_name=u"Назва")
    leader=models.OneToOneField('Student',
	null=True,
	blank=True,
	on_delete=models.SET_NULL,
	verbose_name=u"Староста")

    notes=models.TextField(
	blank=True,
	verbose_name=u"Додаткові нотатки")
    def __unicode__(self):
      if self.leader:
	return u"%s(%s %s)"%(self.title, self.leader.first_name,self.leader.last_name)
      else:
	return u"%s"%(self.title,)
