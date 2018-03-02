from django.contrib.auth.models import AbstractUser
from django.db import models

from GZ_OA import settings


class UserProfile(AbstractUser):
    employee_name = models.CharField(max_length=50, verbose_name="员工姓名", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=7,
                              choices=(
                                  ("mule", "男"),
                                  ("fe_mule", "女"),
                                  ("un_know", "保密")),
                              default="un_know")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)

    position = models.OneToOneField('Position', on_delete=models.CASCADE, default="", null=True)
    section = models.OneToOneField('Section', on_delete=models.CASCADE, default="", null=True)
    superior = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="", null=True)

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.employee_name


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"职位名称", null=False)
    describe = models.TextField(verbose_name="职位描述")
    level = models.IntegerField(verbose_name=u"级别", null=False)

    class Meta:
        verbose_name = u"职位"
        verbose_name_plural = verbose_name


class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"部门名称", null=False)
    describe = models.TextField(verbose_name="部门描述")

    class Meta:
        verbose_name = u"部门"
        verbose_name_plural = verbose_name