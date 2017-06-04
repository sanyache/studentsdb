# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.core.urlresolvers import reverse
from .models.students import Student
from .models.groups import Group
from .models.exam import Exam
from  django.forms import ModelForm,ValidationError
from functools import partial
from django.forms.models import modelformset_factory
# Register your models here.
class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        """Check if student is leader in any group.

        If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups)>0 and    self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи.',
                code='invalid')

        return self.cleaned_data['student_group']
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket',
        'notes']
    form = StudentFormAdmin
    def get_changelist_formset(self, request, **kwargs):
	defaults = {
	    "formfield_callback": partial(super(StudentAdmin,self).formfield_for_dbfield, request=request),
	    "form": StudentFormAdmin,
	}
	defaults.update(kwargs)
	return modelformset_factory(Student,
				    extra=0,
				    fields=self.list_editable, **defaults)


    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})

class GroupFormAdmin(ModelForm):
    def clean_leader(self):
	students = Student.objects.filter(student_group=self.instance)
	if self.cleaned_data['leader'] not in students:
	   raise ValidationError(u'Студент в іншій групі', code='invalid')
	return self.cleaned_data['leader']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['title','leader']
    list_display_links = ['title']
    list_editable = ['leader']
    ordering = ['title']
    list_per_page = 10
    search_fields = ['leader']
    form = GroupFormAdmin
    def get_changelist_formset(self, request, **kwargs):
	defaults = {
	    "formfield_callback": partial(super(GroupAdmin, self).formfield_for_dbfield, request=request),
	    "form": GroupFormAdmin,
	}
	defaults.update(kwargs)
	return modelformset_factory(Group,
				    extra=0,
				    fields=self.list_editable, **defaults)
    def view_on_site(self,obj):
	return reverse('groups_edit', kwargs={'pk': obj.id})
    
admin.site.register(Student,StudentAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Exam)