from django.db import models
from django.contrib.auth.models import Permission, User, Group

from django_auth_ldap.backend import LDAPBackend
from django.utils.translation import activate

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def blogger(sender,user,request,**kwargs):
	list = user.groups.all()
	activate('en')
	if "Bloggers" not in list:
		my_group = Group.objects.get(name='Bloggers') 
		my_group.user_set.add(user)
		user.save()
