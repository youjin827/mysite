from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render # 템플릿 사용해 화면 출력할 수 있는 함수

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html', context)
    # question 모델 데이터 question_list 를 HTML 코드로 변환
    return HttpResponse("안녕하세요 pybo 에 온걸 환영")
            # 페이지 응답 할 때 사용하는 장고 클래스.

def detail(request, question_id):
    # pybo 내용 출력
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)