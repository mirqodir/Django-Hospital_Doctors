from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.shortcuts import render

class Post(models.Model):
	name = models.CharField(max_length=200)
	tel = models.CharField(max_length=20)
	info = RichTextField()
	staji = RichTextField()
	talim = RichTextField()
	image = models.ImageField(upload_to='images/',blank=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
	username = models.CharField(max_length=150,null=True)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=250)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.username}"


class Yengliklar(models.Model):
	yanglik = models.TextField()
	ism = models.TextField()
	vaqt = models.TextField()
	Image = models.ImageField(upload_to='images/',blank=True)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.yanglik}"

	def get_absolute_url(self):
		return reverse('post_detaile', args=[str(self.id)])


class TestModel(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/',blank=True)
	info = RichTextField()


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('post_detaile', args=[str(self.id)])



class Postssss(models.Model):
	name = models.CharField(max_length=200)
	tel = models.CharField(max_length=20)
	info = RichTextField()
	staji = RichTextField()
	talim = RichTextField()
	image = models.ImageField(upload_to='images/',blank=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('post_detailss', args=[str(self.id)])