from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url('^$',views.homepage, name='homepage'),

    url('information', views.information, name='info'),
    url('new/info', views.add_info, name = 'add_info'),

    url('post', views.post, name='post'),
    url('view/blog/(\d+)', views.view_blog, name='view_blog'),
    url(r'^new/blogpost$', views.add_post, name='new-blogpost'),

    url('health', views.health, name='health'),
    url('search/', views.search, name = 'search'),
    url('services', views.services, name='service'),

    url('businesses', views.businesses, name='business'),
    url('add/business', views.add_business, name='add_business'),

    url('profile/(\d+)', views.user_profile, name = 'user-profile'),
    url('update/profile', views.update_profile, name = 'update-profile'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)