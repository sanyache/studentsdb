# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.students import Student
from ..models.groups import Group
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import datetime
from django.views.generic import UpdateView,DeleteView
from django.core.exceptions import ValidationError
#from Classes.CustomForm import CustomForm
from django.contrib import messages
def students_list(request):
    students=Student.objects.all()
    order_by=request.GET.get('order_by','')
    if request.method == 'POST':
	if request.POST.get('search_button') is not None:
	    fields=dict(last_name = 'last_name',first_name = 'first_name',ticket= 'tiket')
	    search=request.POST.get('search_student')
	    search_field=request.POST.get('search_field')
	    if search_field == 'last_name':
		 students=Student.objects.filter(last_name__iexact=search)
	    if search_field ==  'first_name':
		students=Student.objects.filter(first_name__iexact=search)
	    if search_field == 'ticket':
		students=Student.objects.filter(ticket__exact=search)
	    if search_field == 'student_group':
		students=Student.objects.filter(student_group__title__iexact=search)
	    if  students  :
	       return render(request,'students/students_list.html',{'students':students} )
	    else:
		return  HttpResponseRedirect(u'%s?status_message=Студента не знайдено' % reverse('home'))
    if order_by in ('last_name','first_name','ticket'):
        students=students.order_by(order_by)
    elif order_by in ('student_group'):
	      students=students.order_by('student_group__title')
    if request.GET.get('reverse','')=='1':
	students=students.reverse()
    paginator=Paginator(students,3)
    page=request.GET.get('page')
    try:
	students=paginator.page(page)
    except PageNotAnInteger:
	    students=paginator.page(1)
    except EmptyPage:
	    students=paginator(paginator.num_pages)
    return render(request,'students/students_list.html',{'students': students})
def students_edit(request,sid):
    return HttpResponse('<h1>Edit students %s</h1>'% sid)
def students_add(request):

    if request.method == "POST":
	if request.POST.get('add_button') is not None:
	    errors={}
	    data={'middle_name':request.POST.get('middle_name'),
		  'notes': request.POST.get('notes')
		    }
	    first_name=request.POST.get('first_name','').strip()
	    if not first_name:
		errors['first_name']=u"Ім'я є обов'язковим"
	    else:
		data['first_name']=first_name
	    last_name=request.POST.get('last_name','').strip()
	    if not last_name:
		errors['last_name']=u"Прізвище є обов'язковим"
	    else:
		data['last_name']=last_name
	    birthday=request.POST.get('birthday','').strip()
	    if not birthday:
		errors['birthday']=u"Дата народження є обов'язковою"
	    else:
		try:
		    datetime.strptime(birthday,'%Y-%m-%d')
		except Exception:
		    errors['birthday']=u"Введіть коректний формат"
		else:
		    data['birthday']=birthday
	    ticket=request.POST.get('ticket','').strip()
	    if not ticket:
		errors['ticket']=u"Номер білету є обов'язковим"
	    else:
		data['ticket']=ticket
	    student_group=request.POST.get('student_group','').strip()
	    if not student_group:
		errors['student_group']=u"Оберіть групу"
	    else:
		groups=Group.objects.filter(pk=student_group)
		if len(groups) !=1:
		    errors['student_group']=u"Оберіть групу з існуючих"
		else:
		    data['student_group']=groups[0]
	    photo=request.FILES.get('photo')
	    if photo:
		data['photo']=photo

	    if not errors:
	      student = Student(**data)
              student.save()
	      return HttpResponseRedirect(u'%s?status_message=Студента успішно додано!'%
					    reverse('home'))
	    else :
		#render form with errors and previous user input
		return render(request, 'students/students_add.html',
		    {'groups': Group.objects.all().order_by('title'),
		     'errors': errors})
	elif request.POST.get('cancel_button') is not None:
	    return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано!' %
					 reverse ('home'))
    else:
	# initial form render
        return render(request,'students/students_add.html',{'groups':Group.objects.all().order_by('title')})
#class StudentUpdateForm(CustomForm):
#    class Meta:
#        model = Student
#        fields = '__all__'
#
#    def __init__(self, *args, **kwargs):
#        super(StudentUpdateForm, self).__init__(*args, **kwargs)
#        self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})
#
#    def clean_student_group(self):
#        group = Group.objects.filter(leader=self.instance)
#        if len(group) > 0 and self.cleaned_data['student_group'] != group[0]:
#            raise ValidationError(u'Студент є старостою іншою групою', code='invalid')
#    	return self.cleaned_data['student_group']
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    fields='__all__'
    def get_success_url(self):
	return u'%s?status_message=Студента успішно збережено!' % reverse('home')

    def post(self,request,*args,**kwargs):
	if request.POST.get('cancel'):
	    return HttpResponseRedirect(
		u'%s?status_message=Редагування студента відмінено!'% reverse('home'))
	else:
	    return super(StudentUpdateView,self).post(request,*args,**kwargs)
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'
    def get_success_url(self):
	return u'%s?status_message=Студента успішно видалино!' % reverse('home')
def students_search(request):
    return render(request,'students/students_search.html')