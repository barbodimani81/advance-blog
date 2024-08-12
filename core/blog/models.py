from django.db import models
from django.contrib.auth import get_user_model

# getting user model object
User = get_user_model()


class Post(models.Model):
    """
    this is class to define posts for blog app
    """
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
