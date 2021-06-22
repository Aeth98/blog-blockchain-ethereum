from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post, UserIp
from .forms import Register
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from datetime import datetime, timedelta

def posts(request):
    response = []
    posts = Post.objects.filter().order_by('-datetime')
    for post in posts:
        response.append(
            {
                'datetime': post.datetime,
                'title': post.title,
                'content': post.content,
                'author': f"{post.user.first_name} {post.user.last_name}",
                'hash': post.hash,
                'txid': post.txid,

            }
        )
    return JsonResponse(response)

def last_posts(request):
    response = []
    time_threshold = timezone.now() - timedelta(hours=1)
    posts = Post.objects.filter(datetime__gte=time_threshold)
    for post in posts:
        response.append(
            {
                'datetime': post.datetime,
                'title': post.title,
                'content': post.content,
                'author' : post.user.username,
            }
        )
    return JsonResponse(response)

def registerpage(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account successfully created.')
            ip_address = get_client_ip(request)
            person = User.objects.get(username=request.POST.get('username'))
            UserIp.objects.create(user=person, ip=ip_address)
            return redirect('loginpage')
    else:
        form = Register()
    return render(request, 'api/registerpage.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            ip = get_client_ip(request)
            login(request, user)
            logged_user = User.objects.get(username=username)
            my_user_ip = UserIp.objects.get(user=logged_user)
            if not(ip == my_user_ip.ip):
                old_ip = my_user_ip.ip
                my_user_ip.ip = ip
                my_user_ip.save()
                messages.info(request, f'We detected a different ip address, your previous ip was {old_ip}, your new ip is {my_user_ip.ip}')
            else:
                messages.info(request, f'Your ip is {my_user_ip.ip}')
            return redirect('post_list')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'api/loginpage.html', {})

def post_list(request):
    if not request.user.is_authenticated:
        return render(request, 'api/login_error.html')
    posts = Post.objects.filter()
    return render(request, 'api/post_list.html', {'posts': posts})

def post_detail(request, pk):
    posts = Post.objects.filter()
    post = get_object_or_404(posts, pk=pk)
    return render(request, 'api/post_detail.html', {'post': post})

@staff_member_required
def users_posts(request):
    posts = Post.objects.filter()
    users = User.objects.filter()
    number_posts = {}
    for user in users:
        number_posts[user] = len(posts.filter(user=user))
    return render(request, 'api/users_posts.html', {'posts': posts, 'users': users, 'number_posts': number_posts})

def user_id(request, id):
    if not request.user.is_authenticated:
        return render(request, 'api/login_error.html')
    users = User.objects.filter()
    user = get_object_or_404(users, id=id)
    posts = Post.objects.filter(user=user)
    return render(request, 'api/user_id.html', {'posts': posts})

def new_post(request):
    forbidden = 'hack'
    if not request.user.is_authenticated:
        return render(request, 'api/login_error.html')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.content.count(forbidden) > 0:
                messages.info(request, f'you used a forbidden word: {forbidden}')
                return render(request, 'api/new_post.html', {'form': form})
            post.user = request.user
            post.datetime = timezone.now()
            post.save()
            post.writeonChain()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'api/new_post.html', {'form': form})

def login_error(request):
    return render(request, 'api/login_error.html', {})

def logoutpage(request):
    logout(request)
    redirect('api/logoutpage.html')
    return render(request, 'api/logoutpage.html', {})

def search_results(request):
    if request.method == 'GET':
        reference = 0
        searched = request.GET['search']
        posts = Post.objects.filter()
        posts_ref = []
        for post in posts:
            if post.content.lower().count(searched.lower()) > 0:
                reference = reference + 1
                posts_ref.append(post)
    return render(request, 'api/search_results.html', {'searched': searched, 'reference': reference, 'posts_ref': posts_ref})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip




