from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from .models import Question, Quiz
from .serializers import QuizSerializer, QuestionSerializer
from .permissions import IsSuperUser


@api_view(['POST'])
def login(request):
    """Login view."""
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return Response(
            {'error': 'Login failed'},
            status=HTTP_401_UNAUTHORIZED
        )
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


class QuestionViewSet(ModelViewSet):
    """Question view set."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsSuperUser, ]


class QuizViewSet(ModelViewSet):
    """Quiz view set."""

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsSuperUser, ]
