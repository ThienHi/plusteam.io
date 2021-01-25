from django.contrib import admin
from .models import Question,Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question','pub_date')

admin.site.register(Question,QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','choice','vote')

admin.site.register(Choice,ChoiceAdmin)