from django.db import models
# from django import User
# Create your models here.

class BlogPost(models.Model):
    # user = models.ForeignKey(
    #     User
    # )
    category = models.ForeignKey(
        'BlogCategory',
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts"
    )
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


class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)  # Optional field for category description

    def __str__(self):
        return self.name
