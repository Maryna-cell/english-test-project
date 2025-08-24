from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import *
from datetime import datetime
from django.utils.timezone import now
import random
from django.shortcuts import render, get_object_or_404


def format_time(seconds):
    """
    Конвертирует количество секунд в формат "минуты:секунды".
    """
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"


class HomePage(View):
    template_name = "index1.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class TestsPage(View):
    template_name = "tests.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'levels': Levels.objects.all()})


class TestingPage(View):
    template_name = "testing.html"

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        selected_level = request.POST.get("level")
        level = Levels.objects.get(level=selected_level)

        questions_for_test = []

        ordered_topics = level.topics.all()

        for topic in ordered_topics:
            count = topic.priority

            if count > 0:
                all_topic_questions = Questions.objects.filter(grammar_topic=topic)

                num_to_sample = min(count, all_topic_questions.count())

                if num_to_sample > 0:
                    selected_questions = random.sample(list(all_topic_questions), k=num_to_sample)
                    questions_for_test.extend(selected_questions)

        return render(
            request,
            self.template_name,
            {
                'level': level,
                'selected_level': selected_level,
                'email': email,
                'questions': questions_for_test
            }
        )


class ResultPage(View):
    template_name = 'result.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        now = datetime.now()
        email = request.POST.get("email")
        selected_level = request.POST.get("selected_level")
        level = Levels.objects.get(level=selected_level)
        used_time_seconds = int(request.POST.get("used_time"))  # Получаем время в секундах
        formatted_used_time = format_time(used_time_seconds)  # Форматируем его

        statistics = {}
        topic_scores = {}
        total_correct_answers = 0
        total_user_correct_answers = 0

        answered_question_ids = [k for k in request.POST.keys() if k.isdigit()]

        questions = Questions.objects.filter(id__in=answered_question_ids).select_related('grammar_topic')

        for question in questions:
            topic_name = question.grammar_topic.grammar_name

            if topic_name not in topic_scores:
                topic_scores[topic_name] = {'correct': 0, 'user': 0}

            correct_answer_ids = {str(answer.id) for answer in question.answers.filter(right_wrong=True)}

            user_input_ids = set(request.POST.getlist(str(question.id)))

            num_correct_answers = len(correct_answer_ids)
            num_user_correct = len(user_input_ids.intersection(correct_answer_ids))

            topic_scores[topic_name]['correct'] += num_correct_answers
            topic_scores[topic_name]['user'] += num_user_correct

            total_correct_answers += num_correct_answers
            total_user_correct_answers += num_user_correct

        for topic_name, scores in topic_scores.items():
            if scores['correct'] > 0:
                statistics[topic_name] = round(100 * scores['user'] / scores['correct'])
            else:
                statistics[topic_name] = 0

        if total_correct_answers > 0:
            total = round(total_user_correct_answers / total_correct_answers * 100)
        else:
            total = 0

        results_instance = Results.objects.create(
            email=email,
            english_level=selected_level,
            time_consumed=used_time_seconds,
            total_score=total,
            topic_score=str(statistics)
        )
        results_instance.save()

        return render(request, self.template_name, {
            'statistics': statistics,
            'total': total,
            'selected_level': selected_level,
            'email': email,
            'used_time': formatted_used_time,  # Используем отформатированное время
            'now': now.strftime("%m/%d/%Y, %H:%M:%S")
        })


class ArticlesPage(View):
    template_name = "articles.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class Articles_ruPage(View):
    template_name = "articles_ru.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class ContactsPage(View):
    template_name = "contacts.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class What_is_advancedPage(View):
    template_name = "what_is_advanced.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class What_is_advanced_ruPage(View):
    template_name = "what_is_advanced_ru.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class How_long_to_learnPage(View):
    template_name = "how_long_to_learn.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class How_long_to_learn_ruPage(View):
    template_name = "how_long_to_learn_ru.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class Index1_ruPage(View):
    template_name = "index1_ru.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class Index1Page(View):
    template_name = "index1.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class MessagePage(View):

    def post(self, request, *args, **kwargs):
        user_e_mail = request.POST.get("user_e_mail")
        user_name = request.POST.get("user_name")
        user_message = request.POST.get("user_message")
        try:
            Message.objects.create(user_e_mail=user_e_mail, user_name=user_name, user_message=user_message)
            return render(request, "feedback_success.html", {})
        except:
            return render(request, "feedback_fail.html", {})