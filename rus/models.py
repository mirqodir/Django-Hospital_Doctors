from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.shortcuts import render


class Postru(models.Model):
	namee = models.CharField(max_length=200)
	tell = models.CharField(max_length=20)
	infoo = RichTextField()
	stajii = RichTextField()
	talimm = RichTextField()
	image = models.ImageField(upload_to='images/',blank=True)


	def __str__(self):
		return self.namee


	def get_absolute_url(self):
		return reverse('post_detailru', args=[str(self.id)])

class Commentru(models.Model):
	username = models.CharField(max_length=150,null=True)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=250)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.username}"


class Yengliklarru(models.Model):
	yanglikk = models.TextField()
	ismm = models.TextField()
	vaqtt = models.TextField()
	imagee = models.ImageField(upload_to='images/',blank=True)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.yanglikk}"

	def get_absolute_url(self):
		return reverse('post_detaileru', args=[str(self.id)])

class TestModelru(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/',blank=True)
	info = RichTextField()


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('post_detaile', args=[str(self.id)])


class TestModelruu(models.Model):
	names = models.CharField(max_length=200)
	images = models.ImageField(upload_to='images/',blank=True)
	infos = RichTextField()


	def __str__(self):
		return self.names

	def get_absolute_url(self):
		return reverse('post_detailrus', args=[str(self.id)])


class DoctorModelru(models.Model):
	names = models.CharField(max_length=200)
	staj_n = RichTextField()
	talim_n = RichTextField()
	images = models.ImageField(upload_to='images/',blank=True)
	infos = RichTextField()


	def __str__(self):
		return self.names

	def get_absolute_url(self):
		return reverse('new_post_detail',args=[str(self.id)])