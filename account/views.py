from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializer import RegistrationSerializer, ActivateSerializer, LoginSerializer, ForgotPasswordSerializer, \
    ForgotPasswordFinalSerializer


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            return Response('Вы успешно зарегистрировались', status=201)


class ActivateView(APIView):
    def post(self, request):
        data = request.data
        serializer = ActivateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Вы успешно прошли активацию', status=201)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно разлогинились')


class ForgotPasswordView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлен код на почту')


class ForgotPasswordFinalView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordFinalSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_pas()
        return Response('Вы успешно поменяли пороль')

