from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mtaaHud.urls')),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header= "MtaaHood Administration"
admin.site.site_title="MtaaHood"
admin.site.index_title="Welcome to MtaaHud Administration"