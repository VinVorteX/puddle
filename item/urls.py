from django.urls import path
from .views import detail, new, delete, edit, items

app_name = 'item'

urlpatterns = [

    path('', items, name='items'),
    path('<int:pk>/', detail, name='detail'),
    path('new/', new, name='new'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/edit/', edit, name='edit'),

]