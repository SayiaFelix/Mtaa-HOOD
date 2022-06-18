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
    # url(r'^new/blogpost$', views.new_blogpost, name='new-blogpost'),
    # url(r'^new/business$', views.new_business, name='new-business'),
    # url(r'^new/notification$', views.new_notification, name = 'new-notification'),
    url('update/profile', views.update_profile, name = 'update-profile'),
    # url(r'^search/', views.search_results, name = 'search_results'),
  
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)