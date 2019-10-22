from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views 

#import password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    url(r'^$', auth_views.PasswordResetView.as_view(),
    {'post_reset_redirect': reverse_lazy('password_reset_done')}, name= 'password_reset'),
    url(r'^done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(),
    {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name="password_reset_confirm"),
    url(r'^complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]