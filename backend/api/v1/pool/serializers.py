from rest_framework.serializers import ModelSerializer
from .models import Pool, Question, AnswerVariant, PoolSession, Answer


class AnswerSimpleSerializer(ModelSerializer):
    class Meta:
        model = Answer
        exclude = ['pool_session']


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerVariantSerializer(ModelSerializer):
    class Meta:
        model = AnswerVariant
        exclude = ['question']


class QuestionSerializer(ModelSerializer):
    answer = AnswerVariantSerializer(many=True, source='question_answer_variants')

    class Meta:
        model = Question
        exclude = ['pool']


class PoolSerializer(ModelSerializer):
    question = QuestionSerializer(many=True, source='pool_questions')

    class Meta:
        model = Pool
        fields = '__all__'


class PoolSessionSerializer(ModelSerializer):
    answer = AnswerSimpleSerializer(many=True, source='pool_session_answers')

    class Meta:
        model = PoolSession
        fields = '__all__'


class PoolSessionStartSerializer(ModelSerializer):
    class Meta:
        model = PoolSession
        fields = ['user_id']


class PoolSessionSimpleSerializer(ModelSerializer):
    class Meta:
        model = PoolSession
        fields = '__all__'
