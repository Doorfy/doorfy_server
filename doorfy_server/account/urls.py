
from django.conf.urls.defaults import patterns, url
from doorfy_server.account.views.account_home import accountHome
from doorfy_server.account.views.account_settings import accountSettings
from doorfy_server.account.views.active import active
from doorfy_server.account.views.forgot_password import forgotPassword
from doorfy_server.account.views.invitation import invitation
from doorfy_server.account.views.login import login
from doorfy_server.account.views.logout import logout
from doorfy_server.account.views.new_password import newPassword
from doorfy_server.account.views.register import register
from doorfy_server.account.views.reset_password import resetPassword
from doorfy_server.account.views.update_nickname import updateNickname



urlpatterns = patterns('',
    url(r'^$', accountHome),
    url(r'^active/$', active),
    url(r'^login/$', login),
    url(r'^register/$', register),
    url(r'^logout/$', logout),
    url(r'^forgot_password/$', forgotPassword),
    url(r'^newpassword/$', newPassword),
    url(r'^settings/$', accountSettings),
    url(r'^reset_password/$', resetPassword),
    url(r'^update_nickname/$', updateNickname),
    url(r'^invitation/$', invitation),
)
