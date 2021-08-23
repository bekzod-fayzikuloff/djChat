from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, MessageReference


def get_user_profile_by_user_pk(pk):
    """ functions which return user_profile or 404 error """
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    return profile


def link_private_message(from_user, message, to_user):
    """
        function which related message_owner to message and message_to and return accounts.models.MessageReference obj
    """
    return MessageReference(message_from=from_user, message=message, message_to=to_user)
