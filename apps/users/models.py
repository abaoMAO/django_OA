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
                              default="un_know", verbose_name="性别")
    address = models.CharField(max_length=100, default="", verbose_name="家庭住址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="联系方式")

    position = models.OneToOneField('Position', on_delete=models.CASCADE, default="", null=True, verbose_name="职位")
    section = models.OneToOneField('Section', on_delete=models.CASCADE, default="", null=True, verbose_name="部门")
    superior = models.OneToOneField(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE, default="", null=True, verbose_name="上级")

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = verbose_name

    def get_anonymous_name(self):
        pass

    def __str__(self):
        return self.employee_name


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"职位名称", null=False)
    describe = models.TextField(verbose_name="职位描述", null=True, default="", blank=True)
    # level = models.IntegerField(verbose_name="级别", default="", blank=True)

    class Meta:
        verbose_name = u"职位"
        verbose_name_plural = verbose_name


class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"部门名称", null=False)
    describe = models.TextField(verbose_name="部门描述", null=True, default="", blank=True)

    class Meta:
        verbose_name = u"部门"
        verbose_name_plural = verbose_name