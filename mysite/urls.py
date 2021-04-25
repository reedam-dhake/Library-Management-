from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('authentication/',include('django.contrib.auth.urls')),
    path('authentication/',include('authentication.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
