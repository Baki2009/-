from django.urls import path
from .views import TaskList, TaskCreate, TaskRetrieve, TaskUpdate, TaskDestroy

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task_list'),
    path('tasks/create/', TaskCreate.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskRetrieve.as_view(), name='task_retrieve'),
    path('tasks/<int:pk>/update/', TaskUpdate.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDestroy.as_view(), name='task_destroy'),
]

