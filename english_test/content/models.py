from django.db import models # Имортировать из модуля/библиотеки django.db атрибут models, который описывет структуру данных
import uuid # Для создания primary key
from django.utils.timezone import now

class Levels(models.Model):
    level = models.CharField(max_length=2, null=True, verbose_name=('Level'))
    instruction = models.TextField(blank=True, null=True, verbose_name=('Insturction'))
    timing = models.IntegerField(default=40)

    def __str__(self):
        #return f'{self.level} {self.instruction}'
        return self.level

class GrammarTopics(models.Model): # Создать первую таблицу GrammarTopics  с названиями разделов грамматики; Model - это переменная атрибута models для описния поля/столбика таблицы
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)# Нужно создавать это поле?
    grammar_name = models.TextField(blank=True, null=True, verbose_name=('Grammar section'))
    level = models.ForeignKey('Levels', on_delete = models.CASCADE, blank=True, null=True, verbose_name=('level'), related_name='topics' )
    priority = models.IntegerField(default=0)  # <-- Добавьте эту строку

    def __str__(self):
        return self.grammar_name

class Questions(models.Model):
    grammar_topic = models.ForeignKey('GrammarTopics', on_delete = models.CASCADE, blank=True, null=True, verbose_name=('Grammar section'), related_name = "questions" )# Aвтоматически удаляет строку из зависимой таблицы, если удаляется связанная строка из главной таблицы
    question = models.TextField(blank=True, null=True, verbose_name=('Questions'))

    def __str__(self):
        return self.question

class Answers(models.Model):
    question = models.ForeignKey('Questions', on_delete = models.CASCADE, blank=True, null=True, verbose_name=('Question'), related_name = "answers")# Автоматически удаляет строку из зависимой таблицы, если удаляется связанная строка из главной таблицы
    text_answer = models.TextField(blank=True, null=True, verbose_name=('Answers')) # Ответ в виде текста
    right_wrong = models.BooleanField() # Правильный ответ или нет
    worth = models.SmallIntegerField() # Вес ответа

    def __str__(self):
        return f'{self.question} {self.text_answer}'

class Results(models.Model):
    #email = models.EmailField()
    #total_right_answers = models.SmallIntegerField() # Общее количесво ответов
    #total_right_student_answers = models.SmallIntegerField() # Общее количество правильных ответов

    email = models.EmailField()
    english_level = models.CharField(max_length=2, null=True)  # Уровень теста
    time_consumed = models.SmallIntegerField(default=0)  # Время затраченное на тест
    topic_score = models.TextField(blank=True, null=True) # Ответ в виде текста # Общее количество правильных ответов по каждой теме
    total_score = models.SmallIntegerField(default=0)  # Общее количество правильных ответов
    date_time = models.DateTimeField(default=now)

class Message(models.Model):
    user_name = models.CharField(max_length=60, null=True)
    user_e_mail = models.EmailField()
    user_message = models.TextField(blank=True, null=True)
    date_time_message = models.DateTimeField(default=now)






