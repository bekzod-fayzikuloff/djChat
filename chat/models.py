import os
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Message(models.Model):
    """ Модель сообщения """
    owner = models.ForeignKey(User,
                              verbose_name='Отправитель',
                              related_name='message',
                              on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=2000, blank=False)
    photo = models.ImageField('Изображение',
                              upload_to='messages/%Y/%m/%d',
                              blank=True)
    voice = models.FileField('Голосовое',
                             upload_to='audio/%Y/%m/%d',
                             blank=True)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Изменен', auto_now=True)
    to_chat = models.ForeignKey('Chat',
                                verbose_name='Чат',
                                related_name='message',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def filename(self):
        return os.path.basename(self.voice.name)

    def __str__(self):
        return f'{self.pk}: {self.owner.first_name}'


class Member(models.Model):
    """ Связующая модель для соединения пользователя с чатами """
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat',
                             verbose_name='Чат',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return f'{self.user.first_name}: {self.chat.name}'


class Chat(models.Model):
    """ Модель чата """
    name = models.CharField('Название', max_length=120)
    description = models.TextField('Описание',
                                   max_length=1000,
                                   blank=True,
                                   null=True)
    slug = models.SlugField('Слаг',
                            unique=True)
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def get_absolute_url(self):
        return reverse('chat:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

