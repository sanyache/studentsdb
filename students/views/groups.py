# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ..models.groups import Group
from django.core.urlresolvers import reverse
from django.views.generic import CreateView,UpdateView,DeleteView
from ..util import paginate, get_current_group


class GroupCreateView(CreateView):
    model = Group
    template_name = 'students/groups_add.html'
    #form_class = GroupCreateForm 
    fields = '__all__'
    def get_success_url(self):
	return u'%s?status_message=Група успішно добавлена!' % reverse('groups')
    def post(self,request,*args,**kwargs):
	if request.POST.get('cancel'):
	    return HttpResponseRedirect(
		    u'%s?status_message=Створення групи відмінено!' % reverse('groups'))
	else:
	    return super(GroupCreateView,self).post(request,*args,**kwargs)
class GroupUpdateView(UpdateView):
	model = Group
	template_name = 'students/group_edit.html'
	fields = '__all__'
	def get_success_url(self):
	    return u'%s?status_message=Групу успішно збережен!' % reverse('groups')    
	def post(self,request, *args,**kwargs):
	    if request.POST.get('cancel'):
		return HttpResponseRedirect(
		    u'%s?status_message=Редагування відмінено!' % reverse('groups'))
	    else:
		return super(GroupUpdateView,self).post(request,*args,**kwargs)
class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'students/groups_delete.html'
	def get_success_url(self):
	    return u'%s?status_message=Групу видалено!' % reverse('groups')
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>'% gid )
def groups_delete(request,gid):
    return HttpResponse('<h1>Delete Group %s</h1>'% gid)
def groups_list(request):
    groups=Group.objects.all()
    order_by=request.GET.get('order_by','')
    if order_by in ('title','leader'):
	groups=groups.order_by(order_by)
	if request.GET.get('reverse', '') == '1':
	    groups=groups.reverse()
    context = paginate(groups, 3, request, {}, var_name='groups')
    return render(request,'students/groups_list.html', context)