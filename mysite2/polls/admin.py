from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        ('질문 입력', {'fields' : ['question_text']}),
        ('날짜 입력', {'fields' : ['pub_date'], 'classes' : ['collapse']})
    ]
    inlines = [ChoiceInline]
    #sort 기준으로 활용할 수 있는 항목 추가
    list_display = ('question_text','pub_date')
    #filter 추가
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)