from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url('^$',views.homepage, name='homepage'),
    url('information', views.information, name='information'),
    url('post', views.post, name='post'),
    url('post/(\d+)', views.view_post, name='view_post'),
    url('health', views.health, name='health'),
    url('services', views.services, name='services'),
    url('businesses', views.businesses, name='businesses'),
  
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)