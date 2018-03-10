__author__ = 'weimin'
__date__ = '2018/3/10 0010 22:36'

import xadmin
from score.models import Question, Questionnaire, AnswerSheet, Answer


class QuestionInline(object):
    model = Question
    extra = 0


class AnswerInline(object):
    model = Answer
    extra = 0


@xadmin.sites.register(Questionnaire)
class QuestionnaireAdmin(object):
    inlines = [QuestionInline]


@xadmin.sites.register(Question)
class QuestionAdmin(object):
    pass


@xadmin.sites.register(AnswerSheet)
class AnswerSheetAdmin(object):
    inlines = [AnswerInline]
    readonly_fields = ('total_score', 'is_active')


@xadmin.sites.register(Answer)
class AnswerAdmin(object):
    readonly_fields = ('answer_sheet', 'question', 'choices', 'text')