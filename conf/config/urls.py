
#from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
#   path('admin/', admin.site.urls),
    path('', include('theme.urls')),
    path("theme/",include('theme.urls')),
    path("fishlist/",include('fishlist.urls')),
    path("analysis/",include('analysis.urls')),
]

# 파일 업로드를 위한 설정
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)