from rest_framework import serializers


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin cant be in email.')

def clean_email2(value):
    if not value.endswith('@gmail.com'):
        raise serializers.ValidationError('email is invalid.')


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(validators=[clean_email, clean_email2])
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be admin.')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords most be match.')
        return data
