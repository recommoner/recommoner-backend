from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    RECOM_ROLES = (
        ('SC', 'Stewarding Commoner'),
        ('EC', 'Exploiting Commoner')
    )
    """
        Django user model - first_name, last_name, email, password,
        groups, user_permissions
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    organization = models.CharField(max_length=400)
    recom_roles = models.CharField(
        max_length=10,
        choices=RECOM_ROLES,
        default='SC'
    )
