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
from info.views import info,like
from django.conf import settings
from django.conf.urls.static import static
from first import views
from comment.views import dongyeop,create_comment,delete_comment,create_recomment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home ,name='home'),
    path('dongyeop/<int:temp_id>', dongyeop, name="dongyeop"),
    path('create_comment/<int:temp_id>',create_comment , name="create_comment"),
    path('delete_comment/<int:com_id>/<int:temp_id>',delete_comment , name="delete_comment"),
    path('create_recomment/<int:temp_id>',create_recomment , name="create_recomment"),
    path('admin/', admin.site.urls),
    path('info/', info, name="info"),
    path('like/', like, name="like"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
