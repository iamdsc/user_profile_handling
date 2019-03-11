from django.db import models

# Create your models here.
class MyFile(models.Model):
	# title of the file
	title = models.CharField(max_length=200)
	# desctiption of the file
	description = models.TextField()
	# owner of the file
	owner = models.CharField(max_length=100, default=None)
	# file upload
	file = models.FileField(upload_to='')

	def __str__(self):
		return self.title

	# overriding default model delete method
	def delete(self, *args, **kwargs):
		self.file.delete()	# deleting file in file system
		super().delete(*args, **kwargs)
