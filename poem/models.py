from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.urls import reverse 
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = RichTextField(blank=True, null=True)
	date_posted = models.DateTimeField(default=timezone.now)
	likes = models.ManyToManyField(User, related_name='poem_posts')
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})