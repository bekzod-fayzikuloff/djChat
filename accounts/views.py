from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Profile
from . import services


def user_profile(request, pk):
    profile = services.get_user_profile_by_user_pk(pk=pk)
    if profile.user == request.user:
        pass  # place for redirect to own profile
    return render(request, 'user/profile.html', {'profile': profile})
