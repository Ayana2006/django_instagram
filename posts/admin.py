from django.contrib import admin
from posts.models import Post,Comments
from posts.models import Post, Comments, Likes, Comment_likes, Answers

# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Comment_likes)
admin.site.register(Answers)
