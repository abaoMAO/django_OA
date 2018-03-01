from django.db import models

# Create your models here.
from django.utils.encoding import smart_str

from users.models import UserProfile


class Questionnaire(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    judges = models.ManyToManyField(UserProfile, verbose_name="评分人")
    players = models.ManyToManyField(UserProfile, verbose_name="受评人")

    def __str__(self):
        return smart_str(self.players.username + "的问卷")

    class Meta:
        verbose_name = u"问卷"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]


class Question(models.Model):
    question_type = models.CharField(max_length=20, verbose_name="评价指标", null=False)
    question_content = models.CharField(max_length=200, verbose_name="评价要素", null=False)
    full_score = models.IntegerField(max_length=100, verbose_name="标准分值", null=False)

    required = models.BooleanField(default=True, help_text="这个问题是否必须回答")

    questionnaire = models.ForeignKey(Questionnaire)
    order_in_list = models.IntegerField(default=1)  # 在问卷列表中的顺序，从1开始
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = u"问题"
        verbose_name_plural = verbose_name


class AnswerSheet(models.Model):
    judge = models.ForeignKey(UserProfile, verbose_name="评分人")
    player = models.ForeignKey(UserProfile, verbose_name="受评人")
    questionnaire = models.ForeignKey(Questionnaire, verbose_name="对应问卷")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)
    total_score = models.IntegerField(max_length=100, verbose_name="总得分", null=False)

    class Meta:
        verbose_name = u"答卷"
        verbose_name_plural = verbose_name


class Answer(models.Model):
    answer_sheet = models.ForeignKey(AnswerSheet)
    question = models.ForeignKey(Question)
    choices = models.IntegerField(max_length=100, verbose_name="得分", null=False)
    text = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = u"答案"
        verbose_name_plural = verbose_name