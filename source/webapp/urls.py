from django.urls import path

from webapp.views.task1 import get_token_view, calculate
from webapp.views.task2 import IndexView

urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
    path('<action>/', calculate, name='calculate'),
    path('', IndexView.as_view(), name='index')
]
