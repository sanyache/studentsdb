# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

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