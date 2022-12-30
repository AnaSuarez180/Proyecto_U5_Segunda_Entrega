from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm

def assign_default_perms(user):
    # Asignar permisos según el rol del usuario
    if user.is_anonymous:
        assign_perm('view_services', user)
    
    elif user.is_normal:
        assign_perm('view_services', user)
        assign_perm('add_paymentuser', user)
    
    elif user.is_admin:
        assign_perm('view_services', user)
        assign_perm('add_paymentuser', user)
        assign_perm('change_paymentuser', user)
        assign_perm('delete_paymentuser', user)

@receiver(post_save, sender=User)
def assign_perms(sender, instance, created, **kwargs):
    if created:
        assign_default_perms(instance)
