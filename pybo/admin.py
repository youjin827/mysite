# 장고 쉘로 수행했던 데이터 저장,수정, 삭제들 Admin 에서 할 수 있다.
# 앱의 모델 관리!
from django.contrib import admin
from .models import Question, Answer

# 검색 항목 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question)
admin.site.register(Answer)