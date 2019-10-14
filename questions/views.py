from django.shortcuts import render, redirect
from .models import Question, Choice
import random

# Create your views here.
def random_question(request):
    questions_list = Question.objects.all()
    id_li = []
    for k in questions_list:
        id_li.append(k.id)
    random_id = random.choice(id_li)

    return redirect('questions:detail', random_id)

def detail(request, id):
    question = Question.objects.get(id=id)
    all_pick = Choice.objects.filter(question=question)
    p1 = 0
    p2 = 0
    for k in all_pick:
        if k.pick == 1:
            p1 += 1
        else:
            p2 += 1
    all_pick_num = p1 + p2
    if all_pick_num != 0:
        p1_percent = (p1 / all_pick_num) * 100
        p1_percent = int(p1_percent)
        p2_percent = (p2 / all_pick_num) * 100
        p2_percent = int(p2_percent)
        context = {
            'question': question,
            'p1_percent': p1_percent,
            'p2_percent': p2_percent,
            'p1': p1,
            'p2': p2,
        }
    else:
        context = {
            'question': question,
        }

    return render(request, 'detail.html', context)

def index(request):
    questions_list = Question.objects.all()

    context = {
        'questions_list': questions_list
        }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content_a = request.POST.get('content_a')
        content_b = request.POST.get('content_b')
        Question.objects.create(title=title , content_a=content_a, content_b=content_b)

        return redirect('questions:index')
    else:
        return render(request, 'create.html')

def update(request, id):
    question = Question.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content_a = request.POST.get('content_a')
        content_b = request.POST.get('content_b')
        question.title = title
        question.content_a = content_a
        question.content_b = content_b
        question.save()
        return redirect('questions:index')
    else:
        context = {
            'question': question
        }
        return render(request, 'update.html', context)

def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    
    return redirect('questions:index')

def choice_create(request, question_id):
    if request.method =="POST":
        question = Question.objects.get(id=question_id)
        comment = request.POST.get('comment')
        pick = request.POST.get('pick')
        
        Choice.objects.create(
            question=question,
            pick=pick,
            comment=comment,
        )

        return redirect('questions:detail',question_id)
    else:
        pass

def choice_delete(request, question_id, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.delete()

    return redirect('questions:detail', question_id)

def choice_nocomment(request, question_id, pick):
    question = Question.objects.get(id=question_id)
    comment = ""
    Choice.objects.create(
            question=question,
            pick=pick,
            comment=comment,
        )
    
    return redirect('questions:detail', question_id)