from django.db import models
from django.utils.text import slugify

from user.models import User


class News(models.Model):
	title = models.CharField(max_length=999)
	content = models.TextField()
	photo = models.ImageField(upload_to='newsphoto/', default='1.jpg')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_news')

	@property

	def likes_counter(self):
		self.likes.user.count()

	def __str__(self):
		return f'{self.author}/{self.title[:20]}'


class Comment(models.Model):
	comment = models.CharField(max_length=99999999999999999999999999)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
	news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_comments')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.comment


class Like(models.Model):
	user = models.ManyToManyField(User)
	news = models.OneToOneField(News, on_delete=models.CASCADE, related_name='likes')

	def __str__(self):
		return f'{self.user}/{self.news.title[:20]}'
