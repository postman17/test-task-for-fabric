from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'id',
        'question',
    )
    list_display = (
        'id',
        'question',
        'type',
        'answers',
        'created_at',
    )


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'id',
        'title',
        'description',
    )
    list_display = (
        'id',
        'title',
        'start_date',
        'end_date',
        'description',
        'get_questions',
        'created_at',
    )

    def get_questions(self, quiz):
        return mark_safe(
            '<br>'.join([str(question) for question in quiz.questions.all()])
        )
    get_questions.short_description = 'Questions'


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'id',
        'question__question',
    )
    list_display = (
        'id',
        'user',
        'quiz',
        'answers',
        'question',
        'created_at',
    )
