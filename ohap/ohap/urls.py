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
from django.contrib.auth.views import LoginView,LogoutView #login
from django.urls import path
from info.views import info
from django.conf import settings
from django.conf.urls.static import static
from first.views import index,pub,create_comment,beer,delete_comment,create_recomment,delete_recomment,like
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index ,name='index'),
    path('pub/<int:mypub_id>', pub, name="pub"),
    path('create_comment/<int:mypub_id>',create_comment , name="create_comment"),
    path('delete_comment/<int:com_id>/<int:mypub_id>',delete_comment , name="delete_comment"),
    path('create_recomment/<int:mypub_id>',create_recomment , name="create_recomment"),
    path('delete_recomment/<int:recom_id>/<int:mypub_id>',delete_recomment, name="delete_recomment"),
    path('beer/<int:mymenu_id>',beer, name='beer'), 
    path('account/sign_up/',account_views.sign_up,name="sign_up"), #회원가입
    path('account/login/',LoginView.as_view(),name="login"), #로그인
    path('account/logout/',LogoutView.as_view(),name="logout"), #로그아웃
    path('like/<int:mylike_id>/<int:mymenu_id>/',like, name='like'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
