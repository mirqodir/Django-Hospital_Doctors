from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Post,Comment,Yengliklar,TestModel,Postssss
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
import requests
from paginator import *
from django.core.paginator import Paginator

class BlogListView(ListView):
	model = Post
	template_name = 'index.html'

class BlogListViews(DetailView):
	model = Postssss
	template_name = 'post_detailss.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class Blog1ListView(ListView):
	model = Post
	template_name = 'about.html'

class Blog2ListView(ListView):
	model = TestModel
	template_name = 'blog.html'
	context_object_name = 'page'

def Blog211ListView(request):
	obj = TestModel.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,4)
	try:
		page = p.page(page_n)
	except EmptyPage:
		page = p.page(1)
	context = {
		'page':page,

	}
	return render(request,'blog.html',context)


	
	model = TestModel
	template_name = 'blog.html'
	context_object_name = 'page'

class Blog22ListView(DetailView):
	model = Yengliklar
	template_name = 'post_detaile.html'


# class Blog221ListView(DetailView):
# 	model = Yengliklar
# 	template_name = 'yengi.html'

class Blog2221ListView(DetailView):
	model = Yengliklar
	template_name = 'blog-details.html'
	context_object_name = 'posts'

class Blog4ListView(ListView):
	model = Post
	template_name = 'doctors.html'


class Blog3ListView(ListView):
	model = Post
	template_name = 'contact.html'

class Blog33ListView(ListView):
	model = Post
	template_name = 'koproq.html'



def telegram_bot_sendtext(bot_message):
	bot_token = '5103339974:AAHI2WTgRRWldbEOr1zfPiWCkAgvRJi8WXw'
	bot_chatID = '708006401'
	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+bot_message
	response = requests.get(send_text)

	return response.json()

def COntactView(request):
	if request.method == 'POST':
		name = request.POST.get('name',None)
		phone = request.POST.get('phone',None)
		email = request.POST.get('email',None)
		message = request.POST.get('message',None)
		user = Comment.objects.create(
			username = name,
			phone = phone,
			email = email,
			message = message
		)
		user.save()
		telegram_bot_sendtext(f"Ismi:{name}\nTelefon raqami:{phone}\nEmail:{email}\nXabar:{message}")
		print(message)
	return render(
	request=request,
	template_name = 'contact.html'
	)




def index(request):
	if 'q' in request.GET:
		q = request.GET['q']
		data = Post.objects.filter(name__icontains=q)
	else:
		data = Post.objects.all()
	context = {
		"data" :data


	}
	return render(request,'index.html',context)



def BlogDetailViewTest(request,news_id):
	detail = get_object_or_404(TestModel,pk=news_id)
	postall = TestModel.objects.all().first()



	data = {
		"postdetail":detail,
		"postall":postall,

	}
	return render(request,"post_detailtest.html",data)












# def index(request):
# 	if request.method == 'GET':
# 		name = request.GET.get('name',None)
# 		user = Search.objects.filter()
# 	print(soz)
# 	return render(request,'index.html',{'q':soz})



# def IndexViews(request):
# 	if not request.user.is_authenticated:
# 		return HttpResponseRedirect(reverse("login"))
# 	search_query =request.GET.get("q")
# 	groups = request.user.student_in_groups.all()

# 	if search_query == None:
# 		recordings = Post.objects.filter(
# 			group__in=groups

# 		).order_by("-id")
# 	else:
# 		recordings = Post.objects.filters(
# 			group__in=groups,
# 			title__contains = search_query
# 			).order_by("-id")

# 	paginator = Paginator(recordings,RECORD_PER_PAGE)
# 	page_number = request.GET.get("page")    
# 	page_obj = paginator.get_page(page_number)


# 	return render(request,"index.html",{"page_obj":page_obj})




