from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user.urls")),
    path('job/', include("job.urls")),
    path('user/', include("N_userProfile.urls")),
    path('company/', include('company_profile.urls')),
    path('apply/', include("appliedJobs.urls")),
    path('saved/', include('savedJobs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
