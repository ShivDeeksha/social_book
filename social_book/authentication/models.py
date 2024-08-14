from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from datetime import date

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    USER_TYPE_CHOICES = (
        ('author', 'Author'),
        ('reader', 'Reader'),
        ('seller', 'Seller'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    public_visibility = models.BooleanField(default=True)
    age = models.IntegerField(editable=False, null=True)
    bio = models.CharField(max_length=500,default="This is my bio.")

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def save(self, *args, **kwargs):
        if self.birth_date:
            self.age = date.today().year - self.birth_date.year
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
