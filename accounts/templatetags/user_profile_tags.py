from django import template
from django.db.models import Q
from django.contrib.auth.models import User
from ..models import Profile, MessageReference

register = template.Library()


@register.simple_tag
def get_user_profile(user: User):
    return Profile.objects.get(user=user)


@register.simple_tag
def get_profile_private_chats(user: User):
    return MessageReference.objects.filter(Q(message_from=user) | Q(message_to=user))