from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class BookName(models.Model):
	name = models.CharField(max_length=200)
	pages = models.IntegerField()
	isbnNumber = models.CharField(max_length=14)
	publisher = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	year = models.IntegerField()
	image = models.ImageField(null=True, blank=True, upload_to="images/")
	available_copies = models.IntegerField()
	summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
	pdf = models.FileField(null=True, blank=True,upload_to='pdfs/')
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('home')


class Student(models.Model):
	user = models.OneToOneField(User,null = True, on_delete=models.CASCADE)
	total_books_due = models.IntegerField(default=0)
	image = models.ImageField(null=True, blank=True, upload_to="images/profile/")
	name = models.CharField(max_length=200,default=0)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Student.objects.create(user=instance,name=instance.username)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.student.save()


class Borrower(models.Model):
	student = models.ForeignKey('Student', on_delete=models.CASCADE)
	book = models.ForeignKey('BookName', on_delete=models.CASCADE)
	issue_date = models.DateTimeField(null=True,blank=True)
	return_date = models.DateTimeField(null=True,blank=True)
	waiting_list = models.BooleanField(default=False)

class Comment(models.Model):
	post = models.ForeignKey(BookName,null= True,on_delete=models.CASCADE,related_name='comments')
	user = models.ForeignKey(User,null= True,on_delete=models.CASCADE)
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)



