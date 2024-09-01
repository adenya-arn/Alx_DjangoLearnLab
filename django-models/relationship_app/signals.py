from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    print(f"Signal triggered: User instance = {instance}")
    if created:
        # Create a new UserProfile instance for the newly created user
        UserProfile.objects.create(user=instance)
    else:
        # Update existing UserProfile if needed
        UserProfile.objects.update_or_create(user=instance)