from django.db import models
from django.core.validators import FileExtensionValidator
class Exam_paper(models.Model) :
    subject = models.CharField(max_length=100,help_text=u"Enter subject...",blank=True)
    Exam_paper = models.FileField(upload_to='UPLOAD/',validators=[FileExtensionValidator(allowed_extensions=['','pdf'])], null=True, default="Null",
    blank=True, help_text=u"Upload paper ")
class AnswerKey(models.Model) :
    subject = models.CharField(max_length=100,help_text=u"Enter Branch_sem...",blank=True)
    Answer_key = models.FileField(upload_to='UPLOAD/',validators=[FileExtensionValidator(allowed_extensions=['','pdf'])], null=True, default="Null",
    blank=True, help_text=u"Upload Answer_key ")