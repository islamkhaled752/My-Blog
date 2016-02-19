from django.db import models
from django.utils import timezone
# Create your models here.
class post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 50)
	content = models.TextField()
	creation_date = models.DateTimeField(default = timezone.now)
	publishing_date = models.DateTimeField(blank = True , null = True)

	def publish(self):
		self.publishing_date = timezone.now()
		self.save()
	def __str__(self):
	    return self.title	