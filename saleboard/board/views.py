from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from board.forms import BdForm
from board.models import Bd, Rubric


def index(request):
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'board/index.html', context)


def rubric_bbs(request, rubric_id):
    current_rubric = Rubric.objects.get(id=rubric_id)
    rubrics = Rubric.objects.all()
    bbs = Bd.objects.filter(rubric=current_rubric)
    context = {'bbs': bbs, 'current_rubric': current_rubric, 'rubrics': rubrics}
    return render(request, 'board/rubric_bbs.html', context)


class BdCreateView(CreateView):
    template_name = 'board/bd_create.html'
    form_class = BdForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(BdCreateView, self).get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
