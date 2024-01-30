from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.ToDoList.models import Task
from apps.ToDoList.serializers import TaskSerializer

class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieve(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreate(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdate(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDestroy(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
