from django import template
from ..models import Profile

register = template.Library()


@register.simple_tag
def get_user_profile(user):
    return Profile.objects.get(user=user)