from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
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