from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from my_conspire import views

urlpatterns=[
        url(r'^welcome', views.welcome, name='welcome'),
        url(r'^$', views.all_feed, name='feed'),
        url(r'^new/profile$', views.new_profile, name='new-profile'),
        url(r'^all_profiles/(?P<profile_id>\d+)', views.all_profiles, name='all_profiles'),
        url(r'^current_user_profile/(?P<profile_id>\d+)', views.current_user_profile, name='current_user_profile'),
        url(r'^new/feed', views.new_feed, name='new-feed'),
        url(r'^all_articles/', views.all_articles, name='all-articles'),
        url(r'^new/article', views.new_article, name='new-article'),
        url(r'^single_article/(?P<id>\d+)', views.single_article, name='single_article'),
        url(r'^questions', views.Questions, name='questions'),
        url(r'^new/question', views.new_question, name='new-question'),
        url(r'^new/answer', views.new_answer, name='new-answer'),
        url(r'^single_question/(?P<id>\d+)', views.single_question, name='single_question'),
        url(r'^answer_for_specific_question/(?P<question_id>\d+)', views.answer_for_specific_question, name='answer_for_specific_question'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)