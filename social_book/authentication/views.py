from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import SignUpForm, SignInForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from books.forms import BookForm
from books.models import Book

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request, user)
            return JsonResponse({'success': True, 'redirect_url': '/authentication/login/'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return JsonResponse({'success': True, 'redirect_url': '/authentication/profile/'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid username or password.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password.'})
    else:
        form = SignInForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    profile_form = ProfileEditForm(request.POST or None, instance=request.user)
    book_form = BookForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if 'update_profile' in request.POST and profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')

        if 'upload_book' in request.POST and book_form.is_valid():
            book = book_form.save(commit=False)
            book.user = request.user
            book.save()
            return JsonResponse({'success': True, 'redirect_url': '#'})

        return JsonResponse({'success': False, 'message': 'Please correct the errors below.'})


    return render(request, 'profile.html', {
        'form': profile_form,
        'book_form': book_form,
        'user': request.user
    })
