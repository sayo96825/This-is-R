from tkinter import Image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
        profile.follows.add([instance.profile])
        profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)                        #* if user model get deleted -> also delete the profile
    image = models.ImageField(default= 'default=jpg', upload_to='profile_pics')
    follows = models.ManyToManyField("self", related_name = "followed_by", symmetrical= False, blank = True)
    skill = models.CharField(max_length=200, null =True, blank =True)

    def __str__(self):
        return f'{self.user.username} '

    # def save(self):
    #     img = Image.open(self.image.path)
    #     if img.height >300 or img.width >300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)