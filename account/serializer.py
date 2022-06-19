from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Адрес почты занят')
        return email

    def validate(self, attrs):
        if attrs.get('password') != attrs.pop('password_confirm'):
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self):
        attrs = self.validated_data
        user = User.objects.create_user(**attrs)
        code = user.generate_activation_code()
        user.send_regis_code(user.email)
        user.send_activ_code(user.email, code)
        return user


class ActivateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    activation = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Вы не зарегестрированы')
        return email

    def validate_activation(self, activation):
        if not User.objects.filter(activation=activation).exists():
            raise serializers.ValidationError('Вы не зарегестрировались')
        return activation

    def validate(self, attrs):
        email = attrs.get('email')
        activation = attrs.get('activation')
        if not User.objects.filter(email=email, activation=activation).exists():
            raise serializers.ValidationError('Пользователь не найден')
        return attrs

    def activate(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.is_active = True
        user.activation = ''
        user.save()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Вы не зарегестрировались')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError('Пароль или email не верны')
        else:
            raise serializers.ValidationError('Заполните все поля')
        attrs['user'] = user
        return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Вы не зарегестрировались')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.generate_activation_code()
        send_mail(
            'Восстановление пароля',
            f'Ваш код подтверждения: {user.activation}',
            'test@gmail.com',
            [email]
        )


class ForgotPasswordFinalSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True)
    forgotcode = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Вы должны быть зарегестрированы')
        return email

    def validate(self, attrs):
        print(attrs.get('password_confirm'))
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def validate_forgotpassword(self, forgotcode):
        if not User.objects.filter(activation=forgotcode).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return forgotcode

    def set_pas(self):
        email = self.validated_data.get('email')
        new_pass = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(new_pass)
        user.activation = ''
        user.save()
