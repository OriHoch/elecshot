from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
)
