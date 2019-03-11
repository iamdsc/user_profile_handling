"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('register', views.register, name='register'),
	path('account', views.account, name='account'),
	path('login', views.login_request, name='login'),
	path('logout', views.logout_request, name='logout'),
	path('files', views.list_file, name='list_file'),
	path('files/<int:pk>/', views.delete_file, name='delete_file'),
	path('files/upload/',views.file_upload, name='file_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)