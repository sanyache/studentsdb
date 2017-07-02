# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import permission_required

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
	# call original initializator
	super(ContactForm, self).__init__(*args,**kwargs)
	
	#this helper object allow us to customize form
	self.helper = FormHelper()

	# form tag attributes
	self.helper.form_class='form-horizontal'
	self.helper.form_method = 'post'
	self.helper.form_action= reverse('contact_admin')

	# twitter bootstrap styles
	self.helper.help_text_inline= True
	self.helper.html5_required= True
	self.helper.label_class= 'col-sm-2 control-label'
	self.helper.field_class= 'col-sm-6'

	# form buttons
	self.helper.add_input(Submit('send_button', u'Надіслатти'))
    from_email = forms.EmailField(
	label = u"Ваша Емейл Адреса")
    subject = forms.CharField(
	label=u"Заголовок листа",
	max_length=128)
    message = forms.CharField(
	label = u"Текст повідомлення",
	max_length=2560,
	widget=forms.Textarea)
@permission_required('auth.add_user')
def contact_admin(request):
	if request.method == 'POST':
	    form = ContactForm(request.POST)
	    if form.is_valid():
		subject = form.cleaned_data['subject']
		message = form.cleaned_data['message']
		from_email = form.cleaned_data['from_email']
		try :
		    send_mail(subject,message,from_email,[ADMIN_EMAIL])
		except Exception:
		    message = u"Під час відправки виникла помилка"
		    logger = loggin.getLogger(__name__)
		    logger.exception(message)
		else :
		    message = u"Повідомлення успішно надіслане"
		return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'),
					    message))
	else:
	    form = ContactForm()
	return render(request, 'contact_admin/form.html',{'form': form})
    

