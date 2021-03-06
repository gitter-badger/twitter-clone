from django.db import models
from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
	text = models.CharField(max_length=200)
	published_date = models.DateTimeField(blank=True, null=True)
	likes = models.IntegerField(null=True);
	author = models.ForeignKey('auth.user', on_delete=models.CASCADE)


class Follow(models.Model):
	follower = 	models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='followers')
	following = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='following')


class Comment(models.Model):
	text = models.CharField(max_length=200)
	published_date = models.DateTimeField(blank=True, null=True)
	tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)


class HashTag(models.Model):
	name = 	models.CharField(max_length=100)
	tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
