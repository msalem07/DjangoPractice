from django.contrib import admin

from .models import Question, Choice

# Register your models here.
#In order to add the foreign relationship of Choice: extra is how many rows it should include
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#If you want to customize the way models are displayed dont use this (although its fine to use)
#admin.site.register(Question)

#use this (makes it so the pub date comes before the question text)
class QuestionAdmin(admin.ModelAdmin):
    #This is enough
    #fields = ['pub_date', 'question_text']

    #You can also order by sections using: First parameter is the title of the section
    fieldsets = [
        (None, { 'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #Add filter capabilities
    list_filter = ['pub_date']
    #Add search capabilities
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)