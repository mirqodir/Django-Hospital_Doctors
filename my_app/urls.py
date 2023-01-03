from django.urls import path
from .views import BlogListView, BlogDetailView,Blog1ListView,Blog4ListView,COntactView,index,Blog2221ListView,Blog33ListView,BlogDetailViewTest,Blog211ListView,BlogListViews
from .import views

urlpatterns = [
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
	path('post/<int:pk>/', BlogListViews.as_view(), name='post_detailss'),
	path('', views.index, name='index'),	
	path('about/', Blog1ListView.as_view(), name='about'),	
	path('blog/', Blog211ListView, name='blog'),	
	path('contact/', COntactView, name='contact'),	
	path('dorctors/', Blog4ListView.as_view(), name='doctors'),	
	path('koproq/', Blog33ListView.as_view(), name='koproq'),	
	# path('Yengliklar/<int:pk>/', Blog22ListView.as_view(), name='post_detailtest'),
	path('i/<int:pk>/', Blog2221ListView.as_view(), name='blog-details'),
	path('post_detailtest/<int:news_id>/', views.BlogDetailViewTest, name='post_detailtest'),
	# path('contact/', Blog3ListView.as_view(), name='contact'),
	# path('search/', IndexViews, name='base'),


]   