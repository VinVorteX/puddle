from django .urls import path

from conversation.views import new_conversation, inbox, detail

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>/', new_conversation, name='new'),
    path('', inbox, name='inbox'),
    path('<int:pk>/', detail, name='detail'),
]