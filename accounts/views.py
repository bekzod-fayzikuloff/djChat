from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . import services

from .models import Profile, MessageReference, MessagePrivate
from .forms import PrivateMessageForm


def user_profile(request, pk):
    this_profile_user = False
    profile = services.get_user_profile_by_user_pk(pk=pk)
    if profile.user == request.user:
        this_profile_user = True
    return render(request, 'user/profile.html', {'profile': profile,
                                                 'this_profile_user': this_profile_user}
                  )


class PrivateMessageView(View):
    form = PrivateMessageForm
    template_name = 'user/messages.html'

    def get(self, request, *args, **kwargs):
        to_user = get_object_or_404(User, pk=kwargs.get('pk'))
        queryset = MessageReference.objects.filter(message_to__in=[request.user, to_user])
        form = self.form()
        return render(request, self.template_name, {'messages': queryset, 'form': form})

    def post(self, request, *args, **kwargs):
        to_user = get_object_or_404(User, pk=kwargs.get('pk'))
        if 'message' in request.POST:  # processing a request for a message form
            form = self.form(request.POST, request.FILES)
            if form.is_valid():
                message = form.save()
                services.link_private_message(from_user=request.user, message=message, to_user=to_user).save()
                return redirect('users:private_message', to_user.pk)
            return self.get(request, *args, **kwargs)
