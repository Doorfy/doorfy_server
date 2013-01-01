#coding:utf-8
from django.conf.urls import patterns, include, url
from doorfy_server import settings
from doorfy_server.home.views import home, about, contact

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'doorfy_server.views.home', name='home'),
    # url(r'^doorfy_server/', include('doorfy_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    
    # 用户帐户
    url(r'^account/', include('doorfy_server.account.urls')),
    # 验证码   
    url(r'^captcha/', include('captcha.urls')),
    # 静态文件
    (r'^style/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)
