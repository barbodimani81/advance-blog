from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('email', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        ("Persmissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("group permissions", {"fields": ("groups", "user_permissions")}),
        ("user activity", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active", "is_superuser")
        }),
    )


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
