from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from user.models import Post


def governance(request):
    if request.user.is_superuser:
        userList = User.objects.filter(is_superuser=False)
        numPost = {}
        for user in userList:
            cont = len(Post.objects.filter(user=user))
            numPost[user.username] = cont
        return render(request, 'governance/governance.html', {'numPost': numPost})
    else:
        return HttpResponse('<h2>You do not have the necessary permissions to access this area</h2>')
