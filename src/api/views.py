from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer, NewSerializer
from news.models import New


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class NewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = New.objects.all()
    serializer_class = NewSerializer
