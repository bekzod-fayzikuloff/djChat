from django.db.models import Q, QuerySet
from . models import Chat, Member, Message


def get_user_chats(user) -> QuerySet:
    """ getting all members """
    member_queryset = Member.objects.filter(user_id=user.pk)
    return member_queryset


def link_message(message: Message, owner, to_chat: Chat) -> Message:
    """ we linking message to massage_owner and to_chat """
    message.owner = owner
    message.to_chat = to_chat
    return message


def is_chat_member(chat_instance: Chat, user) -> bool:
    """ Check user on chat member """
    if chat_instance.member_set.filter(user_id=user.pk):
        return True
    return False


def get_chat_messages(chat_slug) -> QuerySet:
    """ get chat messages """
    return Chat.objects.get(slug=chat_slug).message.filter()


def link_member(member: Member, user, chat: Chat) -> Member:
    member.user = user
    member.chat = chat
    return member


def chat_search_get_method(request) -> list or str:
    query = request.GET.get('q', None)
    if query:
        object_lists = list(Chat.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query)
        ).values())
        if not object_lists:
            object_lists = 'Совпадение не найдено'
    else:
        object_lists = 'Совпадение не найдено'
    return object_lists
