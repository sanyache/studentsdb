# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models.students import Student
from .models.groups import Group
from .models.exam import Exam


@receiver(post_save)
def log_student_updated_added_event(sender, **kwargs):
    logger = logging.getLogger(__name__)
    model = kwargs['instance']
    if model.__class__ is Student:
        if kwargs['created']:
            logger.info("Student added: %s %s (ID: %d)", model.first_name, model.last_name, model.id)
        else:
            logger.info("Student update: %s %s (ID: %d)", model.first_name, model.last_name, model.id)
    elif model.__class__ is Group:
        if kwargs['created']:
            logger.info("Group added: %s (ID: %d)", model.title, model.id)
        else:
            logger.info("Group update: %s (ID: %d)", model.title, model.id)
    elif model.__class__ is Exam:
        if kwargs['created']:
            logger.info("Exam added: %s %s", model.group_exam, model.subject)
        else:
            logger.info("Exam update: %s %s", model.group_exam, model.subject)


@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    logger = logging.getLogger(__name__)
    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
