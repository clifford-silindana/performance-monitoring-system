from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.get_employees, name = "get_employees"),
    path("get_employee/<int:pk>/", views.get_employee, name = "get_employee"),
    path("create_employee/", views.create_employee, name = "create_employee"),
    path("edit_employee/<int:pk>/", views.update_employee, name = "update_employee"),
    path("delete_employee/<int:pk>/", views.delete_employee, name = "delete_employee"),

    path("departmental_videos/<str:department_name>/", views.get_departmental_videos, name = "get_departmental_videos"),
    path("get_assessment/<int:video_id>/", views.get_video_assessment, name = "get_video_assessment"),
    path("assessment_questions/<int:video_id>/", views.get_assessment_questions, name = "get_assessment_questions"),

]
