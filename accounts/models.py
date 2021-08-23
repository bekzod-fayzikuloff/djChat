from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ Create Profile form for adding some customize fields"""
    user = models.OneToOneField(User,
                                verbose_name='Пользователь',
                                on_delete=models.CASCADE)
    photo = models.ImageField('Изображение',
                              upload_to='users/%Y/%m/%d',
                              blank=True)
    bio = models.TextField('О себе',
                           max_length=1000,
                           blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class MessagePrivate(models.Model):
    """ Crete MessagePrivate model for sending message private """
    text = models.TextField('Сообщение', max_length=2000)
    photo = models.ImageField('Изображение',
                              upload_to='private/messages/%Y/%m/%d',
                              blank=True)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Изменен', auto_now=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.text[: 10]


class MessageReference(models.Model):
    """ Model which using for relating message_from_user, message, and message_to_user"""
    message_from = models.ForeignKey(User,
                                     verbose_name='Отправитель',
                                     related_name='message_from',
                                     on_delete=models.PROTECT)
    message = models.ForeignKey(MessagePrivate,
                                verbose_name='Сообщение',
                                on_delete=models.CASCADE)
    message_to = models.ForeignKey(User,
                                   verbose_name='Получатель',
                                   related_name='message_to',
                                   on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Личное сообщение'
        verbose_name_plural = 'Личные сообщения'

    def __str__(self):
        return f'{self.message_from.username}'

