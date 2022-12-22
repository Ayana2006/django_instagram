from django.shortcuts import render, redirect
from users.models import User, Follows 
from django.contrib.auth import authenticate, login
from posts.models import Post

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username = username, email = email,
            phone = phone, profile_image = profile_image)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
    return render(request, 'register.html')
        
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('index')  
    return render(request, 'sign-in.html')

def account(request, id):
    user = User.objects.get(id = id)
    follow_status = Follows.objects.filter(from_user = request.user, to_user = user).exists()
    if request.method == 'POST':
        if 'follow' in request.POST:
            try:
                follow_status = Follows.objects.get(from_user = request.user, to_user = user)
                follow_status.delete()
                return redirect('account', user.id)
            except:
                follow_status = Follows.objects.create(from_user = request.user, to_user = user)
                follow_status.save()
                return redirect('account', user.id)
    context = {
        'user':user,
        'follow_status':follow_status,
    }
    return render(request, 'my_account.html', context)

def edit_profile(request, id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
            username = request.POST.get('username')
            profile_image = request.FILES.get('profile_image')
            description = request.POST.get('description')
            user.username = username
            user.description = description
            user.profile_image = profile_image
            user.save()
            return redirect('account', user.id)
    return render(request, 'edit_profile.html') 

def followers(request,id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
        follower = request.POST.get('follower')
        follow_status = Follows.objects.all().filter(from_user_id = follower, to_user = user)
        follow_status.delete()
        return redirect('followers', user.id)
    context = {
        'user' : user
    }
    return render(request, 'followers.html', context)

def follows(request,id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
        follower = request.POST.get('follower')
        follow_status = Follows.objects.all().filter(from_user_id = user.id, to_user_id = follower)
        follow_status.delete()
        return redirect('follows', user.id)
    context = {
        'user' : user
    }
    return render(request, 'follows.html', context)



            

        
    