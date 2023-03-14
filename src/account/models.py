from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from account.managers import CustomerManager


class UserAccount(AbstractBaseUser, PermissionsMixin):
    class USER_TYPES(models.IntegerChoices):
        DRIVER = 1, "Driver"
        CARGO_OWNER = 2, "Cargo Owner"

    phone_number = PhoneNumberField(_("phone number"), max_length=16, blank=False)
    first_name = models.CharField(_("name"), max_length=150)
    last_name = models.CharField(_("surname"), max_length=150)
    email = models.EmailField(_("email address"), max_length=100, unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES.choices, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        return f"{self.phone_number}_{self.first_name}_{self.last_name}"


class UserDriverProfile(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name="driver_profile")
    city = models.CharField(max_length=120, blank=True)
    avatar = models.ImageField(default="default.png", upload_to="media/avatars")
    birth_date = models.DateField(null=True)


class UserCargoProfile(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name="cargo_profile")
    city = models.CharField(max_length=120, blank=True)
    avatar = models.ImageField(default="default.png", upload_to="media/avatars")
    birth_date = models.DateField(null=True)
