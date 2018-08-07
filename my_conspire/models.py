from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=100, blank=True, null=True)
    status = models.TextField(max_length=140, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    content = models.TextField(max_length=100, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='commented_by')

    def __str__(self):
        return self.content


class Article(models.Model):
    article_photo = models.ImageField(upload_to='articles/')
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=600, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='author')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=100, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='asked_by')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=100, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='answered_by')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answer_for')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.title


class Feed(models.Model):
    content = models.TextField(max_length=100, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='posted_by')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.content

