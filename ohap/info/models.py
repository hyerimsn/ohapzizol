from django.db import models

class Beer(models.Model):
    pubname = models.TextField(null=True)
    beername = models.TextField(null=True)
    beerimage = models.ImageField(default = "null")
    # like = models.ForeignKey(like, on_delete=models.CASCADE)
    # like_count = models.PositiveIntegerField(default=0)
    taste = models.TextField(null=True)
    information = models.TextField(null=True)
    price = models.TextField(null=True)
    alcohol = models.TextField(null=True)

    def __str__(self):
        return self.beername

# class Like(models.Model):
#      = models.ManyToManyField('Beer')
#     created_at = models.DateTimeField(auto_now = True)

#     def __str__(self):
#         return self.created_at
   

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nickname = models.TextField(max_length=10)

#     like_posts = models.ManyToManyField('Post', blank=True, related_name='like_users')

#     def __str__(self):
#         return self.nickname

# class Post(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#     content = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)

#     like_count = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return self.title
# Create your models here.
