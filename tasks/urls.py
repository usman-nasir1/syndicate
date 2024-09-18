from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskDelete, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name="tasks_list"),
    path('detail/<str:pk>', TaskDetail.as_view() , name="task_detail"),
    path('create', TaskCreate.as_view() , name="task_create"),
    path('delete/<str:pk>', TaskDelete.as_view(), name="task_delete"),
    path('edit/<str:pk>', TaskUpdate.as_view(), name="task_update")
]
