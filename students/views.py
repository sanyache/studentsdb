# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def students_list(request):
    students=(
        {'id': 1,
         'first_name': u'Олександр',
         'last_name' : u'Чемерис',
         'ticket': 235,
	 'image': 'img/che1.jpg'},
	{'id' : 2,
	 'first_name': u'Ірина',
	 'last_name': u'Чемерис',
	 'ticket': 236,
	 'image': 'img/che2.jpg'},
	{'id': 3,
	 'first_name': u'Олександр',
	 'last_name': u'Іваненко',
	 'ticket': 237,
	 'image': 'img/ivan.jpg'},
    )

    return render(request,'students/students_list.html',{'students': students})
def students_edit(request,sid):
    return HttpResponse('<h1>Edit students %s</h1>'% sid)
def students_add(request):
    return HttpResponse('<h1>Add Students </h1>')
def students_delete(request,sid):
    return HttpResponse('<h1>Delete Students %s</h1>'% sid)
def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')
def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>'% gid )
def groups_delete(request,gid):
    return HttpResponse('<h1>Delete Group %s</h1>'% gid)
def groups_list(request):
    return render(request,'students/groups_list.html',{})
def journal(request):
    students = (
        {'id': 1,
         'first_name': u'Олександр',
         'last_name': u'Чемерис',
         'ticket': 235,
         'image': 'img/che1.jpg'},
        {'id': 2,
         'first_name': u'Ірина',
         'last_name': u'Чемерис',
         'ticket': 236,
         'image': 'img/che2.jpg'},
        {'id': 3,
         'first_name': u'Олександр',
         'last_name': u'Іваненко',
         'ticket': 237,
         'image': 'img/ivan.jpg'},
    )

    return render(request,'students/journal.html',{'range':range(30),'students':students})