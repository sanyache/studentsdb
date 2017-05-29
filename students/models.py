# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    class Meta(object):
	verbose_name=u"Студент"
	verbose_name_plural=u"Студенти"
    first_name=models.CharField(
	max_length=256,
	blank=False,
	verbose_name=u"Ім'я")
    last_name=models.CharField(
	max_length=256,
	blank=False,
	verbose_name=u"Прізвище")
    middle_name=models.CharField(
	max_length=256,
	blank=True,
	verbose_name=u"Дата народження",
	null=True)
    birthday=models.DateField(
	blank=False,
	verbose_name=u"Дата народження",
	null=True)
    student_group=models.ForeignKey('Group',
	verbose_name=u"Група",
	blank=False,
	null=True,
	on_delete=models.PROTECT)
    photo=models.ImageField(
	blank=True,
	verbose_name=u"Фото",
	null=True)
    ticket=models.CharField(
	max_length=256,
	blank=False,
	verbose_name=u"Білет")
    notes=models.TextField(
	blank=True,
	verbose_name=u"Додаткові нотатки")
    def __unicode__(self):
	return u"%s %s"%(self.first_name, self.last_name)
class Group(models.Model):
    class Meta(object):
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
class Exam(models.Model):
    class Meta(object):
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