from django.db import models


class Pool(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    is_active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    question = models.CharField('Вопрос', max_length=500)
    single_answer = models.BooleanField('Можно выбрать только один вариант ответа', default=False)
    allow_free_answer = models.BooleanField('Разрешить произвольный ответ', default=False)
    pool = models.ForeignKey(Pool, models.CASCADE, verbose_name='Опрос', related_name='pool_questions')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class AnswerVariant(models.Model):
    answer_variant = models.CharField('Вариант ответа', max_length=500)
    question = models.ForeignKey(
        Question, models.CASCADE, verbose_name='Вопрос', related_name='question_answer_variants')

    def __str__(self):
        return self.answer_variant

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class PoolSession(models.Model):
    user_id = models.IntegerField('ID пользователя')
    date_start = models.DateTimeField('Время начала', auto_now=True, editable=False)
    date_end = models.DateTimeField('Время завершения', blank=True, null=True)
    is_finished = models.BooleanField('Завершен', default=False)

    def __str__(self):
        return f'Сессия: {self.id}'

    class Meta:
        verbose_name = 'Сессия опроса'
        verbose_name_plural = 'Сессии опроса'


class Answer(models.Model):
    question = models.ForeignKey(Question, models.CASCADE, verbose_name='Вопрос')
    answer_variant = models.ForeignKey(AnswerVariant, models.CASCADE, verbose_name='Вариант ответа', blank=True)
    free_answer = models.TextField('Произвольный ответ', blank=True)
    pool_session = models.ForeignKey(
        PoolSession, models.CASCADE, verbose_name='Сессия опроса', related_name='pool_session_answers')

    def __str__(self):
        return self.question.question

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'

