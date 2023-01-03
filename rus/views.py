from django.views.generic import ListView, DetailView,TemplateView
from django.urls import reverse_lazy
from .models import Postru,Commentru,Yengliklarru,TestModelru,DoctorModelru,TestModelruu
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
import requests
from paginator import *
from django.core.paginator import Paginator


class BlogListViewru(ListView):
	model = Postru
	template_name = 'insdexru.html'

class BlogDetailViewru(DetailView):
	model = Postru
	template_name = 'post_detailru.html'

class YengiModelView(DetailView):
	model = TestModelruu
	template_name = 'post_detailrus.html'



class DorctorTestView(DetailView):
	model = DoctorModelru
	template_name = 'new_post_detail.html'



	

class Blog1ListViewru(ListView):
	model = Postru
	template_name = 'aboutru.html'

def Blog222ListViewru(request):												
	obj = TestModelru.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,4)
	try:
		page = p.page(page_n)
	except EmptyPage:
		page = p.page(1)
	context = {
		'pageru': page,

	}
	return render(request,'blogru.html',context)

	# model = TestModelru
	# template_name = 'blogru.html'
	# context_object_name = 'pageru'




class Blog22ListViewru(DetailView):
	model = Yengliklarru
	template_name = 'post_detaileru.html'



class Blog4ListViewru(ListView):
	model = Postru
	template_name = 'doctorsru.html'


class Blog3ListViewru(ListView):
	model = Postru
	template_name = 'contactru.html'

class Blog33ListViewru(ListView):
	model = Postru
	template_name = 'koproqru.html'



def telegram_bot_sendtext(bot_message):
	bot_token = '5103339974:AAHI2WTgRRWldbEOr1zfPiWCkAgvRJi8WXw'
	bot_chatID = '708006401'
	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+bot_message
	response = requests.get(send_text)

	return response.json()

def COntactViewru(request):
	if request.method == 'POST':
		name = request.POST.get('name',None)
		phone = request.POST.get('phone',None)
		email = request.POST.get('email',None)
		message = request.POST.get('message',None)
		user = Commentru.objects.create(
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
	template_name = 'contactru.html'
	)




def indexru(request):
	if 'q' in request.GET:
		q = request.GET['q']
		data = Postru.objects.filter(name__icontains=q)
	else:
		data = Postru.objects.all()
	context = {
		"data" :data


	}
	return render(request,'indexru.html',context)



def BlogDetailViewTestru(request,newss_id):
	detail = get_object_or_404(TestModelru,pk=newss_id)
	postall = TestModelru.objects.all().first()



	data = {
		"postdetail":detail,
		"postall":postall,

	}
	return render(request,"post_detailtests.html",data)



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




