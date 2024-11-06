from django.db import models
# from django import User
# Create your models here.

class BlogPost(models.Model):
    # user = models.ForeignKey(
    #     User
    # )
    title = models.CharField(
        max_length = 255, null = False,
        blank=False
    )
    blog_description = models.TextField(
        null = True, blank = True
    )
    is_active = models.BooleanField(
        default = True
    )
    date = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.title
