from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.all()
# Create your models here.
class Publist(models.Model):
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Menulist(models.Model):
    Publist = models.ForeignKey(Publist, on_delete=models.CASCADE)
    body = models.CharField('메뉴',max_length=50)

    def __str__(self):
        return self.body

class Menudetail(models.Model):
    menulist = models.ForeignKey(Menulist, on_delete=models.CASCADE)
    pubname = models.CharField('펍이름',max_length=50)
    beername = models.CharField('맥주이름',max_length=50)
    beerimage = models.ImageField('이미지')
    likes = models.ManyToManyField(User, blank=True)
    taste = models.TextField('맛')
    information = models.TextField('정보')
    price =models.CharField('가격',max_length= 30)
    alcohol = models.CharField('알콜도수',max_length=30)
    
    def __str__(self):
        return self.beername

class Comment(models.Model):
    post = models.ForeignKey(Publist, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    body = models.CharField('댓글!',max_length=120)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    body = models.CharField('대댓글',max_length=150)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body