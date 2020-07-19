import re

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ()

    # в этой функции мы проверяем размер и формат изображения
    def validate(self, data):
        if 'avatar' in data and data['avatar']:
            file_name = str(data['avatar'])
            match = re.search('(.png$|.jpg$|.jpeg$|.gif$)', file_name)
            if len(data['avatar']) > 2000000 or match is None:
                raise ValidationError('Avatar must be in one of [.png, .jpg, .jpeg, .gif] format, and max 2mb size!!!')
        return data
