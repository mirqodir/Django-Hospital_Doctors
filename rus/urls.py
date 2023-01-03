from django.urls import path
from rus.views import BlogListViewru,indexru,Blog33ListViewru,BlogDetailViewru,Blog1ListViewru,Blog4ListViewru,COntactViewru,Blog222ListViewru,Blog22ListViewru,BlogDetailViewTestru,DorctorTestView,YengiModelView
from .import views


urlpatterns = [
	path('post/<int:pk>/', BlogDetailViewru.as_view(), name='post_detailru'),
	path('posts/<int:pk>/', YengiModelView.as_view(), name='post_detailrus'),
	path('host/<int:pk>/', DorctorTestView.as_view(), name='new_post_detail'),
	path('rus/', views.indexru, name='indexru'),
	path('aboutru/', Blog1ListViewru.as_view(), name='aboutru'),	
	path('blogru/', Blog222ListViewru, name='blogru'),	
	path('contactru/', COntactViewru, name='contactru'),	
	path('dorctorsru/', Blog4ListViewru.as_view(), name='doctorsru'),	
	path('koproqru/', Blog33ListViewru.as_view(), name='koproqru'),	
	path('post/<int:pk>/', Blog22ListViewru.as_view(), name='post_detaileru'),
	path('post_detailtests/<int:newss_id>/', views.BlogDetailViewTestru, name='post_detailtests'),
	# path('contact/', Blog3ListView.as_view(), name='contact'),
	# path('search/', IndexViews, name='base'),

	]   



