# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ..models.exam import Exam
from django.core.urlresolvers import reverse
from django.views.generic import CreateView,UpdateView,DeleteView
#class GroupCreateForm(ModelForm):
#    class Meta:
#	model = Group
#	fields = '__all__'
class ExamCreateView(CreateView):
    model = Exam
    template_name = 'students/exams_add.html'
    #form_class = GroupCreateForm
    fields = ['teacher','group_exam','subject']
    def get_success_url(self):
	return u'%?status_message=Екзамен успішно добавлений!' % reverse('exam')
    def post(self,request,*args,**kwargs):
	if request.POST.get('cancel'):
	    return HttpResponseRedirect(
		    u'%s?status_message=Створення екзамену відмінено!' % reverse('exam'))
	else:
	    return super(ExamCreateView,self).post(request,*args,**kwargs)
class ExamUpdateView(UpdateView):
	model = Exam
	template_name = 'students/exam_edit.html'
	fields = '__all__'
	def get_success_url(self):
	    return u'%s?status_message=Екзамен успішно збережений!' % reverse('exam')
	def post(self,request, *args,**kwargs):
	    if request.POST.get('cancel'):
		return HttpResponseRedirect(
		    u'%s?status_message=Редагування відмінено!' % reverse('exam'))
	    else:
		return super(ExamUpdateView,self).post(request,*args,**kwargs)
class ExamDeleteView(DeleteView):
	model = Exam
	template_name = 'students/exams_delete.html'
	def get_success_url(self):
	    return u'%s?status_message=Екзамен видалено!' % reverse('exam')
def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>'% gid )
def groups_delete(request,gid):
   return HttpResponse('<h1>Delete Group %s</h1>'% gid)
def exam(request):
    exams=Exam.objects.all()
    order_by=request.GET.get('order_by','')
    if order_by in ('date_exam','group_exam'):
	exams=exams.order_by(order_by)
	if request.GET.get('reverse', '') == '1':
	    exams=exams.reverse()
    return render(request,'students/exam.html',{'exams':exams})