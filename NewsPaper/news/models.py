from django.db import models


# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_relation = models.OneToOneField(User)
    author_rating = models.FloatField(default=0.0)


class Category(models.Model):
    category_name = models.CharField(unique=True)


class Post(models.Model):
    post_relation = models.OnetToManyField(Author)
    article_choice = models.CharField(default="статья")
    creation_date = models.DateTimeField(auto_now_add=True)
    post_category_relation = models.ManyToMany(Category, through='PostCategory')
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_rating = models.FloatField(default=0.0)


class PostCategory(models.Model):
    post_category_post_relation = models.OnetToManyField(Post)
    post_category_category_relation = models.OnetToManyField(Category)


class Comments(models.Model):
    comments_post_relation = models.OnetToManyField(Post)
    comments_user_relation = models.OnetToManyField(User)
    comments_text = models.TextField()
    text_creation_time = models.DateTimeField(auto_now_add = True)
    comments_rating = models.FloatField(default = 0.0)

