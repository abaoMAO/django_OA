# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import AnswerSheet


class ScoreView(View):
    # 获取当前用户的所有活跃的问题
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            answer_sheets = AnswerSheet.objects.filter(judge=user.id).exclude(is_active=False)
            return render(request, "score.html", {
                "answer_sheets": answer_sheets,
            })
        else:
            return render(request, "user_login.html")


class AnswerSheetView(View):
    # 具体的答卷
    def get(self, request, as_code):
        user = request.user
        if user.is_authenticated:
            answer_sheet = AnswerSheet.objects.get(id=as_code)
            questionnaire = answer_sheet.questionnaire
            questions = questionnaire.question_set.all()
            return render(request, "answer_sheet.html", {
                "answer_sheet": answer_sheet,
                "questionnaire": questionnaire,
                "questions": questions,
            })
        else:
            return render(request, "user_login.html")

    def post(self, request, as_code):
        user = request.user
        if user.is_authenticated:

            answer_sheets = AnswerSheet.objects.filter(judge=user.id).exclude(is_active=False)
            return render(request, "score.html", {
                "answer_sheets": answer_sheets,
            })
        else:
            return render(request, "user_login.html")