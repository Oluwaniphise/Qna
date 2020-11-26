from django.contrib import admin
from .models import Question, Answer, Profile

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Answer)
admin.site.register(Profile)
