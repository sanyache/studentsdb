"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from students.views import students,groups,journal,exam,contact_admin
from settings import DEBUG,MEDIA_ROOT
from django.conf.urls.static import static
from students.views.students import StudentUpdateView,StudentDeleteView
from students.views.groups import GroupCreateView,GroupUpdateView,GroupDeleteView
from students.views.exam import ExamCreateView,ExamUpdateView,ExamDeleteView
#from students.views.contact_admin import 
urlpatterns = [
    url(r'^$',students.students_list,name='home'),
    url(r'^groups/$',groups.groups_list,name='groups'),

    url(r'^students/add/$',students.students_add,name='students_add'),
    url(r'^students/search/$',students.students_search,name='students_search'),
    url(r'^students/(?P<pk>\d+)/delete/$',StudentDeleteView.as_view(),name='students_delete'),
    url(r'^students/(?P<pk>\d+)/edit/$',StudentUpdateView.as_view(),name='students_edit'),

    url(r'^groups/add/$',GroupCreateView.as_view(),name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$',GroupUpdateView.as_view(),name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$',GroupDeleteView.as_view(),name='groups_delete'),

    url(r'^journal/$',journal.journal,name='journal'),

    url(r'^exam/$',exam.exam,name='exam'),
    url(r'^exam/add/$',ExamCreateView.as_view(),name='exam_add'),
    url(r'^exam/(?P<pk>\d+)/delete/$',ExamDeleteView.as_view(),name='exam_delete'),
    url(r'^exam/(?P<pk>\d+)/edit/$',ExamUpdateView.as_view(),name='exam_edit'),

    url(r'^contact_admin/$', contact_admin.contact_admin, name='contact_admin'),

    url(r'^admin/',admin.site.urls),
]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns+=[
	    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT})
	]
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
