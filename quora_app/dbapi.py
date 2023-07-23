from django.db.models import QuerySet
from .models import Question,Answer

def get_all_questions() -> QuerySet:
    return Question.objects.all()

def get_question(*args,**kwargs) -> Question:
    return Question.objects.get(*args,**kwargs)

def get_answer(*args,**kwargs) -> Answer:
    return Answer.objects.get(*args,**kwargs)

def filter_answer(*args,**kwargs) -> QuerySet:
    return Answer.objects.filter(*args,**kwargs)

def filter_question(*args,**kwargs) -> QuerySet:
    return Question.objects.filter(*args,**kwargs)