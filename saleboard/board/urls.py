from django.urls import path

from board.views import index, rubric_bbs, BdCreateView

urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', rubric_bbs, name='rubric_bbs'),
    path('add/', BdCreateView.as_view(), name='add'),
]
