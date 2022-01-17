from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin

from .models import Pool, PoolSession, Answer
from .serializers import PoolSerializer, PoolSessionStartSerializer, PoolSessionSimpleSerializer, PoolSessionSerializer, \
    AnswerSerializer


class PoolListView(ListAPIView):
    """
    Опросы

    Получение списка активных опросов
    """

    queryset = Pool.objects.filter(is_active=True).all()
    serializer_class = PoolSerializer


class PoolSessionCreateView(CreateAPIView):
    """
    Создать сессию

    Начать сессию опроса

    Указываем user_id, в момент создания сессии автоматически подставится время и дата начала опроса
    На выходе получем структуру с pool_session.id которая понадобится для завершения сессии
    """

    queryset = PoolSession.objects.all()
    serializer_class = PoolSessionStartSerializer

    @swagger_auto_schema(responses={201: PoolSessionSimpleSerializer()})
    def post(self, request, *args, **kwargs):
        self.serializer_class = PoolSessionSimpleSerializer
        return self.create(request, *args, **kwargs)


class PoolSessionEditView(GenericAPIView, UpdateModelMixin):
    """
    Завершить сессию

    Завершить сессию опроса
    Завершить сессию можно по pool_session.id, в момент закрытия сессию автоматически
    подставится время и дата завершения сессии
    """

    queryset = PoolSession.objects.filter(is_finished=False).all()

    @swagger_auto_schema(responses={200: PoolSessionSimpleSerializer()})
    def patch(self, request, *args, **kwargs):
        self.serializer_class = PoolSessionSimpleSerializer
        data = self.serializer_class(self.get_object()).data
        data.update({
            'date_end': timezone.now(),
            'is_finished': True,
        })
        self.data = data
        return self.update(self, request, *args, **kwargs)


class PoolSessionListView(ListAPIView):
    """
    Сессии

    Получить список завершенных сессий для конкретного пользователя
    """

    queryset = PoolSession.objects.filter(is_finished=True).all()
    serializer_class = PoolSessionSerializer
    lookup_field = 'user_id'


class AnswerCreateView(CreateAPIView):
    """
    Ответ

    Инициировать ответ на вопрос опроса
    """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
