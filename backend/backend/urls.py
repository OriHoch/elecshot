from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
)
