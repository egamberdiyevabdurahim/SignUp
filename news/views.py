from django.shortcuts import render, redirect

from user.models import User
from .models import News, Comment
from .forms import NewsForm, CommentForm


def create(request):
	form = NewsForm()
	if request.method == 'POST':
		form = NewsForm(data = request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'create.html', {'form':form})
	return render(request, 'create.html', {'form':form})


def edit(request, id):
	news = News.objects.get(id=id)
	form = NewsForm(instance=news)
	if request.method =='POST':
		form = NewsForm(instance=news, data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'create.html', {'form':form})
	return render(request, 'create.html', {'form':form})


def delete(request, id):
	news = News.objects.get(id=id)
	news.delete()
	return redirect('home')


def opennews(request, id):
	news = News.objects.get(id=id)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(data=request.POST)
		if form.is_valid():
			# form.save()
			comment = form.cleaned_data['comment']
			Comment.objects.create(
					comment = comment,
					news = news,
					user = request.user
				)
			return redirect('home')
 		# return render(request, 'opennews.html', {'opennews':news, 'form':form})
	return render(request, 'opennews.html', {'opennews':news, 'form':form})


# def create_comment(request, id):
# 	if request.method == 'POST':
# 		form = CommentForm(data=request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('opennews', id)


