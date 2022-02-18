from django.contrib import admin
from django.urls import path
from tasks.views import delete_task_view, task_view, add_task_view, delete_task_view, complete_task_view, completed_tasks_view, all_tasks_view, index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view),
    path("tasks/", task_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    path("complete_task/<int:index>/", complete_task_view),
    path("completed_tasks/", completed_tasks_view),
    path("all_tasks/", all_tasks_view)
]
