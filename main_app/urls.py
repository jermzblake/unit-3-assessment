from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_index, name='index'),
    path('/add_task', views.add_task, name='add_task'),
    path('<int:pk>/delete', views.TaskDelete.as_view(), name='tasks_delete')
]