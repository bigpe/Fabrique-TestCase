from django.contrib import admin

from django_app.utils.admin_utils import NotModifyMixin, get_objects_change_links, get_object_change_link
from .models import Pool, Question, AnswerVariant, PoolSession, Answer

from nested_admin import NestedStackedInline, NestedModelAdmin


class AnswerVariantInline(NestedStackedInline):
    model = AnswerVariant
    extra = 0


class QuestionInline(NestedStackedInline):
    model = Question
    inlines = [AnswerVariantInline]
    extra = 0


class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 0
    max_num = 0


class PoolAdmin(NestedModelAdmin):
    inlines = [QuestionInline]
    list_display = ['name', 'description', 'questions', 'is_active']
    list_editable = ['is_active']

    def questions(self, obj):
        return get_objects_change_links(obj, 'pool_questions', lookup_field='question')

    questions.short_description = 'Вопросы'


class PoolSessionAdmin(NotModifyMixin, NestedModelAdmin):
    inlines = [AnswerInline]


class AnswerAdmin(NotModifyMixin, NestedModelAdmin):
    list_display = ['question', 'pool_session_link']

    def pool_session_link(self, obj):
        return get_object_change_link(obj, 'pool_session', lookup_field='id')


class QuestionAdmin(NestedModelAdmin):
    list_display = ['question', 'pool_link', 'single_answer', 'allow_free_answer']
    model = Question
    inlines = [AnswerVariantInline]
    extra = 0

    def pool_link(self, obj):
        return get_object_change_link(obj, 'pool')

    pool_link.short_description = 'Опрос'


admin.site.register(Pool, PoolAdmin)
admin.site.register(PoolSession, PoolSessionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
