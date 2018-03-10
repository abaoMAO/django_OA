from django.contrib.auth.models import AbstractUser
from django.db import models

from GZ_OA import settings


class UserProfile(AbstractUser):
    employee_name = models.CharField(max_length=50, verbose_name="员工姓名", default="")
    section = models.OneToOneField('Section', on_delete=models.CASCADE, default="", null=True, verbose_name="部门")
    employee_number = models.IntegerField(verbose_name="员工编号")
    position = models.OneToOneField('Position', on_delete=models.CASCADE, default="", null=True, verbose_name="职位")
    gender = models.CharField(max_length=7,
                              choices=(
                                  ("mule", "男"),
                                  ("fe_mule", "女"),
                                  ("un_know", "保密")),
                              default="un_know", verbose_name="性别")
    ethnic = models.CharField(max_length=100, default="", verbose_name="民族")
    birthday = models.DateField(verbose_name="出生年月", null=True, blank=True)

    # entry_time = models.DateField(verbose_name="入司日期", null=True, blank=True)
    # formal_time = models.DateField(verbose_name="转正日期", null=True, blank=True)

    # address = models.CharField(max_length=100, default="", verbose_name="现居住详细地址")
    # mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="联系方式")
    # huji_type = models.CharField(max_length=11, null=True, blank=True, verbose_name="户籍类型")
    # bank_number = models.IntegerField(verbose_name="银行卡号")
    # bank_name = models.CharField(max_length=20, null=True, blank=True, verbose_name="开户行名称")

    # emergency_contact = models.CharField(max_length=5, null=True, blank=True, verbose_name="紧急联系人")
    # emergency_mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="联系人联系方式")
    # emergency_relationship = models.CharField(max_length=11, null=True, blank=True, verbose_name="与联系人关系")
    #
    # contract_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="劳动合同流水号")
    #
    # email_is_active = models.BooleanField(default=False, verbose_name="邮箱是否建立")
    # have_certificate = models.BooleanField(default=False, verbose_name="是否有会计从业资格证")

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