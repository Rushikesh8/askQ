from django.urls import path
from quora_app.views import (custom_signup,
                             custom_login,
                             question_list,
                             post_question,
                             answer_question,
                             like_answer,
                             custom_logout)
urlpatterns = [
    path('signup/', custom_signup, name='signup'),
    path('login/', custom_login, name='login'),
    path('questions/', question_list, name='questions'),
    path('post-question/', post_question, name='post-question'),
    path('answer-question/<int:question_id>/', answer_question, name='answer-question'),
    path('like-answer/<int:answer_id>/', like_answer, name='like-answer'),
    path('logout/', custom_logout, name='logout'),
 ]
