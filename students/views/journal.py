# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from ..models.students import  Student
from ..models.monthjournal import MonthJournal 
from ..util import paginate, get_current_group



class JournalView(TemplateView):
    template_name = 'students/journal.html'

    def get_context_data(self, **kwargs):
        context = super(JournalView, self).get_context_data(**kwargs)
        if self.request.GET.get('month'):
            month = datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
        else:
            today = datetime.today()
            month = date(today.year, today.month, 1)
        next_month = month+relativedelta(months=1)
        prev_month = month-relativedelta(months=1)
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['next_month'] = next_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['cur_month'] = month.strftime('%Y-%m-%d')
        context['month_verbose'] = month.strftime('%B')
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear, mmonth)[1]
        context['month_header'] = [
            {'day': d, 'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
            for d in range(1, number_of_days+1)]
        current_group = get_current_group(self.request)
        if kwargs.get('pk'):
            queryset = [Student.objects.get(pk=kwargs['pk'])]
        elif current_group:
            queryset = Student.objects.filter(student_group=current_group).order_by('last_name')
        else:
            queryset = Student.objects.all().order_by('last_name')
        update_url = reverse('journal')
        students = []
        for student in queryset:
            try:
                journal = MonthJournal.objects.get(student=student, date=month)
            except Exception:
                journal = None
            days = []
            for day in range(1, number_of_days+1):
                days.append({
                    'day': day,
                    'present': journal and getattr(journal, 'present_day%d' % day, False) or False,
                    'date': date(myear, mmonth, day).strftime('%Y-%m-%d'),
                })
            students.append({
                'fullname': u'%s %s' % (student.last_name, student.first_name),
                'days': days,
                'id': student.id,
                'update_url': update_url,
            })
        context = paginate(students, 3, self.request, context, var_name='students')
        return context
    def post(self, request, *args, **kwargs):
        data = request.POST
        current_date = datetime.strptime(data['date'],'%Y-%m-%d').date()
        month = date(current_date.year, current_date.month,1)
        present = data['present'] and True or False
        student = Student.objects.get(pk=data['pk'])
        journal = MonthJournal.objects.get_or_create(student=student, date=month)[0]
        setattr(journal, 'present_day%d' % current_date.day, present)
        journal.save()
        return JsonResponse({'status':'success'})


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

    return render(request, 'students/journal.html', {'range': range(30), 'students': students})
