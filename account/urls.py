from django.urls import path

from account.views import RegistrationView, ActivateView, LoginView, LogoutView, ForgotPasswordView, \
    ForgotPasswordFinalView

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('activate/', ActivateView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('forgotpassword/', ForgotPasswordView.as_view()),
    path('forgotpassworfinal/', ForgotPasswordFinalView.as_view()),
]