from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        if email:
            user = self.model(email=email, **extra_fields)
        else:
            user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def authenticate(self, phone, password, **extra_fields):
        if phone is not None and password is not None:
            try:
                user = User.objects.get(phone=phone)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
        return None


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format +919999999999."
                                         " Up to 10 digits allowed.")
    phone = models.CharField('Phone', validators=[phone_regex], max_length=10, unique=False, null=True)
    is_seller = models.BooleanField(default=False)  # Seller account check
    REQUIRED_FIELD = ['username', 'phone']

    objects = UserManager()

    # class PhoneOTP(models.Model):
    #    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
    #                                 message="Phone number must be entered in the format +919999999999."
    #                                         " Up to 10 digits allowed.")
    #    phone = models.CharField(validators=[phone_regex], max_length=10, unique=True)
    #    otp = models.CharField(max_length=9, blank=True, null=True)
    #    count = models.IntegerField(default=0, help_text='Number of otp_sent')
    #    validated = models.BooleanField(default=False,
    #                                    help_text='If it is true, that means user have validate otp correctly in second API')
    #   otp_session_id = models.CharField(max_length=120, null=True, default="")
    #    username = models.CharField(max_length=20, blank=True, null=True, default=None)
    #    email = models.CharField(max_length=50, null=True, blank=True, default=None)
    #    password = models.CharField(max_length=100, null=True, blank=True, default=None)

    # def _str_(self):
    #    return str(self.phone) + ' is sent ' + str(self.otp)
