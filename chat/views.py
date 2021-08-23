from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Chat, Message, Member
from .forms import MemberChatForm, MessageSendForm
from . import services


@login_required
def index(request):
    """ view for render `index` page """
    member_data = services.get_user_chats(request.user)
    if request.method == 'GET':
        queryset = services.chat_search_get_method(request=request)
        if request.is_ajax():
            return JsonResponse({'chats': queryset}, safe=False)
    return render(request, 'chat/index.html', {'members_data': member_data})


@login_required
def chat_detail(request, slug):
    """ Chat detail view """
    chat = get_object_or_404(Chat, slug=slug)
    chat_messages = services.get_chat_messages(chat_slug=slug)
    is_member = services.is_chat_member(chat, request.user)
    if request.method == 'POST':

        if 'message' in request.POST:  # processing a request for a message form
            message_form = MessageSendForm(request.POST, request.FILES, prefix='message')
            if message_form.is_valid():
                new_message = message_form.save(commit=False)
                services.link_message(message=new_message, owner=request.user, to_chat=chat).save()
                return redirect(chat.get_absolute_url())

        elif 'member' in request.POST:  # processing a request for a member form
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


class MemberLeaveView(View):
    """ class for realize user leaving from some chat """

    def get(self, request, *args, **kwargs):
        chat = get_object_or_404(Chat, slug=kwargs.get('chat_slug'))
        member = get_object_or_404(Member, user_id=kwargs.get('pk'), chat=chat)
        member.delete()
        return redirect(chat.get_absolute_url())