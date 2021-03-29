from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse
import math
from .models import Post


def homePage(request):
    if request.method == 'POST':
        message = request.POST
        if 'hack' in message['msg'] or 'Hack' in message['msg']:
            return HttpResponse('<h2>Error: you can not use the term "hack" or "Hack".</h2>')
        else:
            new_post = Post(user=request.user, content=message['msg'])
            new_post.setDate()
            new_post.save()
            response = []
            posts = Post.objects.filter().order_by('-published_date')
            for post in posts:
                response.append({
                    'content': post.content,
                    'author': f"{post.user}",
                    'published_date': post.published_date
                })

            return render(request, 'user/home_page.html', {'post': response})
    else:
        response = []
        posts = Post.objects.filter().order_by('-published_date')
        for post in posts:
            response.append({
                'content': post.content,
                'author': f"{post.user}",
                'published_date': post.published_date
            })
        return render(request, 'user/home_page.html', {'post': response})


def last_h_Posts(request):
    lastPosts = []
    now = timezone.now()
    posts = Post.objects.filter().order_by('-published_date')
    for post in posts:
        diff = now - post.published_date
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds / 60)
            lastPosts.append({
                'author': f"{post.user}",
                'content': post.content,
                'published_date': post.published_date,
                'minutesAgo': minutes
            })
        else:
            continue
    return JsonResponse(lastPosts)


def searchWord_form(request):
    return render_to_response('searchWord_form.html')

def searchWord(request):
    word = request.GET.get('q', '')
    posts = Post.objects.filter().order_by('-published_date')
    w = word.replace('<', '')
    w = w.replace('>', '')
    count = 0
    for post in posts:
        if w in post.content:
            count += 1
    return HttpResponse(f'The word {w} appeared {count} times in the posts.')
