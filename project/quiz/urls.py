from django.urls import path, include
from rest_framework import routers
from .views import login, QuizViewSet, QuestionViewSet


router = routers.DefaultRouter()
router.register('quiz', QuizViewSet, basename='quiz')
router.register('question', QuestionViewSet, basename='question')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', login),
]
