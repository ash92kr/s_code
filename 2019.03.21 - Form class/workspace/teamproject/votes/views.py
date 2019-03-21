from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'votes/index.html', context)
    
def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        select_a = request.POST.get('select_a')
        select_b = request.POST.get('select_b')
        image_a = request.FILES.get('image_a')
        image_b = request.FILES.get('image_b')
        
        question = Question(title=title, select_a=select_a, select_b=select_b, image_a=image_a, image_b=image_b)
        question.save()
        return redirect('votes:detail', question.pk)
    else:
        return render(request, 'votes/new.html')
        
def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    answers = question.answer_set.all()
    if len(answers) == 0:
        rate_a = 0
        rate_b = 0
        str_rate_a = '0%'
        str_rate_b = '0%'
    else:
        rate_a = round(len(answers.filter(pick='0'))/len(answers)*100, 2)
        str_rate_a = str(rate_a)+'%'
        rate_b = round(len(answers.filter(pick='1'))/len(answers)*100, 2)
        str_rate_b = str(rate_b)+'%'
    context = {
        'question': question,
        'answers': answers,
        'rate_a': rate_a,
        'rate_b': rate_b,
        'str_rate_a': str_rate_a,
        'str_rate_b': str_rate_b,
    }
    return render(request, 'votes/detail.html', context)
    
def delete(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method  == 'POST':
        question.delete()
        return redirect('votes:index')
    else:
        return redirect('votes:detail', question.pk)
        
def edit(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == 'POST':
        question.title = request.POST.get('title')
        question.select_a = request.POST.get('select_a')
        question.select_b = request.POST.get('select_b')
    
        question = Question(title=question.title, select_a=question.select_a, select_b=question.select_b)
        question.save()
        return redirect('votes:detail', question.pk)
    else:
        context = {
            'question': question,
        }
        return render(request, 'votes/edit.html', context)
        
def answers_create(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    pick = request.POST.get('pick')
    comment = request.POST.get('comment')
    
    answer = Answer(pick=pick, comment=comment, question=question)
    answer.save()
    return redirect('votes:detail', question.pk)

def answers_delete(request, question_pk, answer_pk):
    question = Question.objects.get(pk=question_pk)
    answer = Answer.objects.get(pk=answer_pk)
    
    if request.method == 'POST':
        answer.delete()
        return redirect('votes:detail', question.pk)
    else:
        return redirect('votes:detail', question.pk)