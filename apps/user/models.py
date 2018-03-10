from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    employee_name = models.CharField(max_length=50, verbose_name="员工姓名", default="")

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = verbose_name