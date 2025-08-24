from django.contrib import admin
from .models import *


# Фильтр для раздела GrammarTopics
class GrammarTopicsLevelFilter(admin.SimpleListFilter):
    title = 'level'  # <-- Имя, которое появится в админ-панели
    parameter_name = 'level'

    def lookups(self, request, model_admin):
        levels = Levels.objects.all().order_by('level')
        return [(lvl.pk, lvl.level) for lvl in levels]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(level__pk=self.value())
        return queryset


# Фильтр для раздела Questions
class QuestionsLevelFilter(admin.SimpleListFilter):
    title = 'level'  # <-- Имя, которое появится в админ-панели
    parameter_name = 'level'

    def lookups(self, request, model_admin):
        levels = Levels.objects.all().order_by('level')
        return [(lvl.pk, lvl.level) for lvl in levels]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(grammar_topic__level__pk=self.value())
        return queryset


# Встроенная модель для ответов
class AnswerInline(admin.TabularInline):
    model = Answers
    extra = 1


# Встроенная модель для вопросов
class QuestionInline(admin.TabularInline):
    model = Questions
    extra = 1


# Регистрируем модели с фильтрами и полями для поиска
@admin.register(Levels)
class LevelsAdmin(admin.ModelAdmin):
    list_display = ('level', 'instruction', 'timing')
    search_fields = ('level',)


@admin.register(GrammarTopics)
class GrammarTopicsAdmin(admin.ModelAdmin):
    list_display = ('grammar_name', 'level', 'priority')
    list_filter = (GrammarTopicsLevelFilter,)  # <-- ИСПОЛЬЗУЕМ НОВЫЙ ФИЛЬТР
    search_fields = ('grammar_name',)
    inlines = [QuestionInline]


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'grammar_topic')
    list_filter = (QuestionsLevelFilter, 'grammar_topic')  # <-- ИСПОЛЬЗУЕМ НОВЫЙ ФИЛЬТР И ОСТАВЛЯЕМ СТАРЫЙ
    search_fields = ('question',)
    inlines = [AnswerInline]


@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text_answer', 'right_wrong')
    list_filter = ('question',)
    search_fields = ('text_answer',)


# Регистрируем остальные модели
admin.site.register(Results)
admin.site.register(Message)