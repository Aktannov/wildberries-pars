from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils.crypto import get_random_string


class UserManager(BaseUserManager):
    def _create(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email не может быть пустым')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation = models.CharField(max_length=8, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    def generate_activation_code(self):
        code = get_random_string(8)
        self.activation = code
        self.save()
        return code

    @staticmethod
    def send_regis_code(email):
        send_mail('Регистрация:', 'Вы успешно зарегестрировались', 'test@gmail.com', [email])

    @staticmethod
    def send_activ_code(email, code):
        send_mail('Ваш код активации:', code, 'test@gmail.com', [email])


# posts = User.objects.all()
# some = posts[1]
# print(User.objects.filter(is_staff=True))
# activation = 'Q1tda0Qf'
# print(User.objects.filter(activation=activation))

