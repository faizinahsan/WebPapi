from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Dosen,Mahasiswa
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if instance.is_student:
        if created:
            Mahasiswa.objects.create(user = instance)
        instance.mahasiswa.save()
    elif instance.is_teacher:
        if created:
            Dosen.objects.create(user = instance)
        instance.dosen.save()
        # Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
    # instance.profile.save()

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	print('****', created)
# 	if instance.is_intern:
# 		InternProfile.objects.get_or_create(user = instance)
# 	else:
# 		HRProfile.objects.get_or_create(user = instance)
	
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	print('_-----')	
# 	# print(instance.internprofile.bio, instance.internprofile.location)
# 	if instance.is_intern:
# 		instance.intern_profile.save()
# 	else:
# 		HRProfile.objects.get_or_create(user = instance)