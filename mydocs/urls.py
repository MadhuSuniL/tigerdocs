"""mydocs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from docs_app.views import *
urlpatterns = [
    path('', start),
    path('post_rec/<pk>', postfor_record),
    path('getfor_rec/<pk>', getfor_rec),
    path('post_doc', postfor_doc),
    path('getfor_doc', getfor_doc),
    path('delete_last_rec/<pk>', delfor_rec),
    path('delete_last_doc/', delfor_doc),
    path('docadmin/', admin.site.urls),
]
