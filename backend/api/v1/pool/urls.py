from django.urls import path

from .views import PoolListView, PoolSessionCreateView, PoolSessionEditView, PoolSessionListView, AnswerCreateView

urlpatterns = [
    path('', PoolListView.as_view()),
    path('session/start/', PoolSessionCreateView.as_view()),
    path('session/end/<int:pk>', PoolSessionEditView.as_view()),
    path('session/<int:user_id>', PoolSessionListView.as_view()),
    path('answer/', AnswerCreateView.as_view()),
]
