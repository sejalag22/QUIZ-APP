#application url router
from django.urls import path
from quizapp.views import homePage

urlpatterns = [
    path('quizapp/', homePage),
]
