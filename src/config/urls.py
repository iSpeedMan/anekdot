from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.common.urls')),
    path('admin/', admin.site.urls),
    path('mems/', include('apps.slaider.urls'))
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
urlpatterns += staticfiles_urlpatterns()
