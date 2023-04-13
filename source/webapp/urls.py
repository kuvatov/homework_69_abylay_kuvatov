from django.urls import path

from webapp.views import get_token_view, calculate

urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
    path('<action>/', calculate, name='calculate')
]
