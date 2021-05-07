from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Question,Choice, AccessibleChoice, User

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question','pub_date')

admin.site.register(Question,QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','choice','vote')

admin.site.register(Choice,ChoiceAdmin)


# @admin.register(AccessibleChoice)
class AccessibleChoiceAdmin(ImportExportModelAdmin):
    list_display = ('id','access', 'user', 'email', 'status')
    class Meta:
        model = AccessibleChoice
        fields = ('access', 'user')
        
admin.site.register(AccessibleChoice,AccessibleChoiceAdmin)