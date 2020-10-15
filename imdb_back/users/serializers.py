from rest_framework import serializers
from imdb_back.users.models import User
import string
from random import choice
from imdb_back.users.email_sender import EmailSender

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'profile_picture']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        chars = string.digits
        random =  ''.join(choice(chars) for _ in range(4))
        user.verification_code = random
        user.save()
        email_sender = EmailSender()
        email_sender.send_email(user.email, user.verification_code)
        return user


