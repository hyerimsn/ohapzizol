"""ohap URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from first.views import index,pub,create_comment,beer,delete_comment,create_recomment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index ,name='index'),
    path('pub/<int:mypub_id>', pub, name="pub"),
    path('create_comment/<int:mypub_id>',create_comment , name="create_comment"),
    path('delete_comment/<int:com_id>/<int:mypub_id>',delete_comment , name="delete_comment"),
    path('create_recomment/<int:mypub_id>',create_recomment , name="create_recomment"),
    path('beer/<int:mymenu_id>',beer, name='beer')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
