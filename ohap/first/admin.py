from django.contrib import admin
from .models import Publist,Comment,Menulist,Menudetail
# Register your models here.
admin.site.register(Publist)
admin.site.register(Comment)
admin.site.register(Menulist)
admin.site.register(Menudetail)