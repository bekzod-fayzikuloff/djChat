from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Chat, Message, Member
from .forms import MemberChatForm, MessageSendForm
from . import services


@login_required
def index(request):
    member_data = services.get_user_chats(request.user)
    return render(request, 'chat/index.html', {'member_data': member_data})


@login_required
def chat_detail(request, slug):
    chat = get_object_or_404(Chat, slug=slug)
    chat_messages = services.get_chat_messages(chat_slug=slug)
    is_member = services.is_chat_member(chat, request.user)
    if request.method == 'POST':
        if 'message' in request.POST:
            message_form = MessageSendForm(request.POST, prefix='message')
            if message_form.is_valid():
                new_message = message_form.save(commit=False)
                services.link_message(message=new_message, owner=request.user, to_chat=chat).save()
                return redirect(chat.get_absolute_url())
        elif 'member' in request.POST:
            member_form = MemberChatForm(request.POST, prefix='member')
            if member_form.is_valid():
                new_member = member_form.save(commit=False)
                services.link_member(member=new_member, user=request.user, chat=chat).save()
                return redirect(chat.get_absolute_url())
    else:
        message_form = MessageSendForm(prefix='message')
        member_form = MemberChatForm(prefix='member')
    return render(request,
                  'chat/detail.html',
                  {
                      'messages': chat_messages,
                      'chat': chat,
                      'is_member': is_member,
                      'message_form': message_form,
                      'member_form': member_form
                  }
                  )


class SearchChatView(ListView):
    model = Chat
    template_name = 'chat/search.html'
    context_object_name = 'chats'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Chat.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query)
        )
        return object_list
