from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile


def get_user_profile_by_user_pk(pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    return profile
