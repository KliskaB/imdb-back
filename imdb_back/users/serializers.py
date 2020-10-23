from rest_framework import serializers
from imdb_back.users.models import User
import string
from random import choice
from imdb_back.users.email_sender import EmailSender
from rest_framework.exceptions import ValidationError

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
        reciever_email = user.email
        verification_code = user.verification_code
        subject = "Verify your email address"
        email_sender.send_email(reciever_email, subject, verification_code, "verification-email.html")
        return user


class VerifyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['verification_code']
    
    def validate(self, data):
        user = self.context['request'].user
        if(data["verification_code"] != user.verification_code):
            raise ValidationError('Code invalid')
        return data

    def save(self, user, **kwargs):
        user.is_verified = True
        user.save()
        return user



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'is_verified', 'profile_picture']


