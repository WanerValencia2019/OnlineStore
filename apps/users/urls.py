 
from django.urls import path,re_path
from django.contrib.auth.views import LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.decorators import login_required

#Views
from .views import LoginView, RegisterView, configuration

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('configuration/',login_required(configuration,login_url='login'),name='configuration'),
    path(r'reset/password_reset', PasswordResetView.as_view(template_name='resetPassword/password_reset_form.html',html_email_template_name='resetPassword/password_reset_email.html'), name='password_reset'),
    path(r'reset/password_reset_done', PasswordResetDoneView.as_view(template_name='resetPassword/password_reset_done.html'), name='password_reset_done'),
    re_path(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='resetPassword/password_reset_confirm.html'), name='password_reset_confirm'),
    path(r'reset/done', PasswordResetCompleteView.as_view(template_name='resetPassword/password_reset_complete.html'), name='password_reset_complete'),
]