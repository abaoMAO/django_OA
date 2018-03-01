from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models
from scores.models import Questionnaire


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(("mule", u"男"), ("femule", u"女"), ("unknow", u"保密")), default="unknow")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # position = models.ForeignKey(Position)
    # section = models.ForeignKey(Section)
    # superior = models.ForeignKey(UserProfile)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def get_anonymous_name(self):
        pass

    def __unicode__(self):
        return self.username


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"名称", null=False)
    describe = models.TextField(verbose_name="职位描述")
    level = models.IntegerField(max_length=3, verbose_name=u"级别", null=False)

    class Meta:
        verbose_name = u"职位"
        verbose_name_plural = verbose_name


class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"名称", null=False)
    describe = models.TextField(verbose_name="部门描述")

    class Meta:
        verbose_name = u"部门"
        verbose_name_plural = verbose_name