from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils.encoding import smart_str


class UserProfile(AbstractUser):
    # employee_name = models.CharField(max_length=50, verbose_name="员工姓名", default="")
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True, verbose_name="所属部门")
    position = models.ForeignKey('Position', on_delete=models.CASCADE, null=True, blank=True, verbose_name="职位")

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return smart_str(self.last_name + self.first_name+"  " + self.username)


class Department(models.Model):
    name = models.CharField(max_length=20, verbose_name="部门名称")
    description = models.TextField(verbose_name="部门描述", null=True, blank=True)

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=20, verbose_name="职位名称")
    description = models.TextField(verbose_name="职位描述", null=True, blank=True)

    class Meta:
        verbose_name = "职位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

