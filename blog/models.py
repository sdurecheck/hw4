from django.db import models

class PostQuerySet(models.QuerySet):
	def published(self):
		return self.filter(is_public = True)

class Post(models.Model):
	author = models.CharField(max_length=100)
	title = models.CharField(max_length=100)	
	text = models.TextField()
	is_public = models.BooleanField(default=True)
	pub_date = models.DateTimeField(auto_now_add=True)
	upd_date = models.DateTimeField(auto_now=True)
	objects = PostQuerySet.as_manager()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.post

	class Meta:
		ordering = ['-pub_date']

class Author(models.Model):
	author = models.CharField(max_length=100)
	text = models.CharField(max_length=400)
	pub_date = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post')
	
	def __unicode__(self):
		return self.post

