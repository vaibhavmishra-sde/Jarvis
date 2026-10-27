from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("c/<uuid:conversation_id>/", views.index, name="conversation_detail"),
    path("new/", views.new_chat, name="new_chat"),
    path("delete/<uuid:conversation_id>/", views.delete_chat, name="delete_chat"),
    path("api/chat/", views.chat_api, name="chat_api"),
    path("api/health/", views.health_api, name="health_api"),
    path("api/metrics/", views.metrics_api, name="metrics_api"),
    path("api/productivity/", views.productivity_api, name="productivity_api"),
    path("api/productivity/write/", views.productivity_write_api, name="productivity_write_api"),
    path("api/productivity/todos/<int:todo_id>/", views.todo_api, name="todo_api"),
    path("api/briefing/", views.briefing_api, name="briefing_api"),
    path("api/skills/", views.skills_api, name="skills_api"),
    path("api/conversations/<uuid:conversation_id>/export/", views.export_conversation, name="export_conversation"),
]

