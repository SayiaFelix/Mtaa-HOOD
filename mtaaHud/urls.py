from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url('^$',views.homepage, name='homepage'),
    url('information', views.information, name='info'),
    url('post', views.post, name='post'),
    url('post/(\d+)', views.view_post, name='view_post'),
    url('health', views.health, name='health'),
    url('services', views.services, name='service'),
    url('businesses', views.businesses, name='business'),
    url('profile/(\d+)', views.user_profile, name = 'user-profile'),
    url('new/post', views.add_post, name='add_post'),
    url('new/business', views.add_business, name='add_business'),
    url('new/info', views.add_info, name = 'add_info'),
    url('update/profile', views.update_profile, name = 'update-profile'),
    url('search/', views.search, name = 'search'),
  
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)