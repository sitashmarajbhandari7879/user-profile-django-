# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
	MALE='M'
	FEMALE='F'
	CHOICES=((MALE,"MALE"),(FEMALE,"FEMALE"),)
	user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one field enable one profile to one user
	country = models.CharField(max_length=20, blank=True, null =  True)
	city = models.CharField(max_length=20, blank=True, null =  True)
	street_name = models.CharField(max_length=20, blank=True, null =  True)
	street_number = models.CharField(max_length=20, blank=True, null =  True) # this is extra field to user model
	gender=models.CharField(max_length=10,choices=CHOICES,null=True,blank=True)
	bio = models.CharField(max_length= 500, blank=True, null=True)
	birth_date = models.DateField(blank=True, null=True)
	contact = models.IntegerField(blank=True, null=True)
	job=models.CharField(max_length= 100, blank=True, null=True)
	profile_picture=models.ImageField(blank=True,null=True,upload_to='Images_Quora/%Y-%m-%d')

	class Meta:
		db_table = 'auth_profile' #create customize dB table 


	def __str__(self):
		return self.user.username



@receiver(post_save, sender=User) #signal used to create a object related to user instance
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #signal used to save a object related to user instance
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()