from django.conf.urls import url, include
from accounts.views import logout, login, register, user_profile
from accounts import urls_reset


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="register"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^password_reset/', include(urls_reset)),
]