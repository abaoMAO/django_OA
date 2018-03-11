# Create your models here.
from django.db import models
from django.utils.encoding import smart_str
from django_OA import settings
from user.models import Department


class Questionnaire(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    type = models.CharField(max_length=20, choices=(
        ("down2up", "下对上"),
        ("up2down", "上对下"),
        ("up2up", "平级")
    ), verbose_name="类型", default="up2up")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="所属部门")
    question = models.ManyToManyField('Question', related_name="questionnaire_level_question", verbose_name="问题")

    def __str__(self):
        return smart_str(self.department.name + "的" + self.type + "的问卷")

    class Meta:
        verbose_name = u"问卷"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]


class Question(models.Model):
    question_type = models.CharField(max_length=20, verbose_name="评价指标", null=False)
    question_content = models.CharField(max_length=200, verbose_name="评价要素", null=False)
    full_score = models.IntegerField(verbose_name="标准分值", null=False)
    # required = models.BooleanField(default=True, help_text="这个问题是否必须回答")
    # questionnaire = models.ForeignKey('Questionnaire', on_delete=models.CASCADE, default="")
    order_in_list = models.IntegerField(default=1)  # 在问卷列表中的顺序，从1开始
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = u"问题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return smart_str(self.question_type + " " + self.question_content)


class AssessmentRelationship(models.Model):
    judge = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='judge',
                              on_delete=models.CASCADE, verbose_name="评分人")
    player = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='player',
                               on_delete=models.CASCADE, verbose_name="受评人")
    questionnaire = models.ForeignKey('Questionnaire',
                                      on_delete=models.CASCADE, verbose_name="对应问卷")
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    modified_at = models.DateTimeField(auto_now=True, editable=False, verbose_name="提交时间")

    class Meta:
        verbose_name = u"考勤关系"
        verbose_name_plural = verbose_name

    def __str__(self):
        return smart_str(self.judge.first_name + "对" + self.player.first_name + "的评价")


class AnswerSheet(models.Model):
    answer_sheet_base = models.ForeignKey('AssessmentRelationship', on_delete=models.CASCADE, verbose_name="对应问卷")
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    modified_at = models.DateTimeField(auto_now=True, editable=False, verbose_name="提交时间")
    is_active = models.BooleanField(default=True)
    total_score = models.CharField(max_length=5, verbose_name="总得分", default="-1")

    class Meta:
        verbose_name = u"答卷"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]

    def __str__(self):
        return smart_str(str(self.created_at.month) + "月" + str(self.answer_sheet_base) + "的评价")


class Answer(models.Model):
    answer_sheet = models.ForeignKey('AnswerSheet',
                                     on_delete=models.CASCADE, verbose_name="对应答卷")
    question = models.ForeignKey('Question',
                                 on_delete=models.CASCADE, verbose_name="对应问题")
    choices = models.CharField(max_length=5, verbose_name="得分",
                               null=True, blank=True, default="")
    text = models.TextField(verbose_name="备注", null=True, blank=True, default="")

    class Meta:
        verbose_name = u"答案"
        verbose_name_plural = verbose_name

