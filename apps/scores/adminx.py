__author__ = 'weimin'
__date__ = '2018/3/3 0003 18:35'

import xadmin
from .models import *


# class GlobalSetting(object):
#     site_title = "奇维OA后台管理系统"
#     site_footer = "奇维科技"
#     menu_style = "accordion"


class QuestionnaireAdmin(object):
    pass


class QuestionAdmin(object):
    pass


class AnswerSheetAdmin(object):
    pass


class AnswerAdmin(object):
    pass


xadmin.site.register(Questionnaire, QuestionnaireAdmin)
xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(AnswerSheet, AnswerSheetAdmin)
xadmin.site.register(Answer, AnswerAdmin)
