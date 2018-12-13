import rest_auth.serializers
from rest_framework import serializers
from django.contrib.auth import get_user_model


class LoginSerializer(rest_auth.serializers.LoginSerializer):
    def get_fields(self):
        print("custom LoginSerializer")
        fields = super(LoginSerializer, self).get_fields()
        fields['email'] = fields['username']
        del fields['username']
        return fields

    def validate(self, attrs):
        attrs['username'] = attrs['email']
        del attrs['email']
        return super(LoginSerializer, self).validate(attrs)


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = get_user_model()
        fields = ('pk', 'email', 'name')
        read_only_fields = ('email', )


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address."))
        return email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def get_cleaned_data(self):
        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        user = get_user_model()
        cleaned_data = self.get_cleaned_data()
        user.create_user(**cleaned_data)
        return user
