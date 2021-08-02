import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .models import Profile
from . import services


def user_profile(request, pk):
    this_profile_user = False
    profile = services.get_user_profile_by_user_pk(pk=pk)
    if profile.user == request.user:
        this_profile_user = True
    return render(request, 'user/profile.html', {'profile': profile,
                                                 'this_profile_user': this_profile_user}
                  )

