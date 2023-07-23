from django.shortcuts import render,redirect
from django.db.models import Q
from quora_app.forms import CustomSignupForm,CustomLoginForm,QuestionForm,AnswerForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from quora_app.dbapi import get_all_questions,get_answer,get_question,filter_answer

def custom_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('questions')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('questions')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def question_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    query = request.GET.get('search',"")
    questions = get_all_questions().filter(Q(title__icontains=query)).order_by('-id')
    answers_liked = list()
    if request.user.is_authenticated:
        answers_liked = filter_answer(likes=request.user)
    return render(request, 'questions.html', {'questions': questions,"answers_liked":answers_liked})


def post_question(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('questions')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

def answer_question(request, question_id):
    if not request.user.is_authenticated:
        return redirect('login')
    question = get_question(id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('questions')
    else:
        form = AnswerForm()
    return render(request, 'answer.html', {'form': form, 'question': question})

def like_answer(request, answer_id):
    if not request.user.is_authenticated:
        return redirect('login')
    answer = get_answer(id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)

    request.user.refresh_from_db()

    return redirect('questions')

def custom_logout(request):
    logout(request)
    return redirect('login')


