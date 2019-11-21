from django.contrib import admin
from .models import Exam_paper,AnswerKey
# Register your models here.
class Exam_paperAdmin(admin.ModelAdmin):
    list_display = ['subject' ]
    search_fields = ('subject' ,)
admin.site.register(Exam_paper , Exam_paperAdmin)
class AnswerKeyAdmin(admin.ModelAdmin):
    list_display = ['subject']
    search_fields = ('subject' ,)
admin.site.register(AnswerKey , AnswerKeyAdmin)