"""disease_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from accounts.views import logout
from accounts.views import sign_in_doctor
from disease_prediction import settings
admin.site.logout = logout

urlpatterns = [
     path('admin/', admin.site.urls),
    path('admin/login/', sign_in_doctor, name='custom_login'),
     path("", include("main_app.urls")),
     path("accounts/", include("accounts.urls")),
     path("", include("chats.urls"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)

admin.site.login = 'custom_login'
admin.site.index_title = "Disease detection system using machine learning "
admin.site.site_header = "Disease detection system using machine learning "
admin.site.site_title = "Disease detection system using machine learning "  