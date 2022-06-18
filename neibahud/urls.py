from django.contrib import admin
from django.urls import path,include
from mtaaHud import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mtaaHud.urls')),
    path('register/',views.register_user,name='register'),
    path('accounts/login/',views.login_user,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header= "MtaaHood Administration"
admin.site.site_title="MtaaHood"
admin.site.index_title="Welcome to MtaaHud Administration"