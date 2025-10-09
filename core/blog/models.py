from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# get user model object
# User = get_user_model()


class Post(models.Model):
    """
    This is a class to define posts for blog app
    """

    image = models.ImageField(upload_to="blog/", null=True, blank=True)
    title = models.CharField(max_length=250)
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True
    )
    status = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["creation_date"]

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.id})


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
