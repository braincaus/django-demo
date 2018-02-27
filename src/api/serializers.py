from django.contrib.auth.models import User, Group
from news.models import New
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email')


class NewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'owner', 'title', 'content')
