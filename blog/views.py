from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from blog.models import BlogUser
from blog.forms import ProfileForm
# Create your views here.
def login_page(request):
    return render(request, 'login.html')
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')  # 登入成功，跳轉到主頁面
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')
def home(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            bloguser = BlogUser(user=user)
            bloguser.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def userlogout(request):
    logout(request)
    return redirect('home')

def edit_profile(request):
    Profilef = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.bloguser)

    if request.method == 'POST':
        if Profilef.is_valid():
            Profilef.save()
            return redirect('about')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'editprofile.html', {
        'Profilefile': Profilef,
        'form': form
    })

def test(request):
    return render(request,'test.html')



def userabout(request):
    user = request.user
    blog_user = BlogUser.objects.get(user=user)
    context={
        'username':user.username,
        'bio':blog_user.bio,
        'headshot':blog_user.headshot
    }
    return render(request,'about.html',context)