# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.core.urlresolvers import reverse
from .models.students import Student
from .models.groups import Group
from .models.exam import Exam
from  django.forms import ModelForm,ValidationError
# Register your models here.
class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        """Check if student is leader in any group.

        If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if groups and    self.cleaned_data['student_group'] != groups[0].title:
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

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})

class GroupFormAdmin(ModelForm):
    def clean_leader(self):
	#students = Student.objects.filter(student_group=self.instance)
	group=self.cleaned_data.get('title')
	students = Student.objects.filter(student_group=group)
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
    def view_on_site(self,obj):
	return reverse('groups_edit', kwargs={'pk': obj.id})
    
admin.site.register(Student,StudentAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Exam)