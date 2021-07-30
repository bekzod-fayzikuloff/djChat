from . models import Chat, Member, Message


def get_user_chats(user):
    member_queryset = Member.objects.filter(user_id=user.pk)
    return member_queryset


def link_message(message: Message, owner, to_chat: Chat):
    message.owner = owner
    message.to_chat = to_chat
    return message


def is_chat_member(chat_instance: Chat, user):
    if chat_instance.member_set.filter(user_id=user.pk):
        return True
    return False


def get_chat_messages(chat_slug):
    return Chat.objects.get(slug=chat_slug).message.filter()


def link_member(member: Member, user, chat: Chat):
    member.user = user
    member.chat = chat
    return member


