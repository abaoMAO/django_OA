__author__ = 'weimin'
__date__ = '2018/3/11 0011 9:56'

import xadmin
from .models import Question, Questionnaire, AnswerSheet, Answer, AssessmentRelationship


class QuestionInline(object):
    model = Question
    extra = 0


class AnswerInline(object):
    model = Answer
    extra = 0


@xadmin.sites.register(AssessmentRelationship)
class AssessmentRelationshipAdmin(object):
    pass


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