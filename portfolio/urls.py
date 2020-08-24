"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django_distill import distill_path
from django.urls import path
import jobs.views
from django.conf import settings
from django.conf.urls.static import static


def get_index():
    return None

def get_detail():
    return None

urlpatterns = [
    path('admin/', admin.site.urls),
    distill_path('',jobs.views.homepage, name='home', distill_func= get_index, distill_file='home.html'),
    distill_path('jobs/<int:job_id>',jobs.views.detail, name='detail',distill_func= get_detail, distill_file='detail.html'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
