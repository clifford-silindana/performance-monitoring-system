from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import EmployeeSerializer, VideoSerializer, AssessmentSerializer, AssessmentQuestionsSerializer

@api_view(["GET"])
def get_employees(request):
    employees = Employee.objects.all()
    serialized_employees = EmployeeSerializer(employees, many = True)
    return Response(serialized_employees.data)

@api_view(["GET"])
def get_employee(request, pk):
    employee = Employee.objects.get(id = pk)
    serialized_employee = EmployeeSerializer(employee, many = False)
    return Response(serialized_employee.data)


@api_view(["POST"])
def create_employee(request):
    serialized_employee = EmployeeSerializer(data = request.data)
    if serialized_employee.is_valid():
        serialized_employee.save()

    return Response(serialized_employee.data)

@api_view(["PUT"])
def update_employee(request, pk):
    data = request.data
    employee = Employee.objects.get(id = pk)
    serialized_employee = EmployeeSerializer(instance = employee, data = data)

    print("VALIDITY", serialized_employee.is_valid())

    if serialized_employee.is_valid():
        serialized_employee.save()
        print("Valid")

    print(serialized_employee)

    return Response(serialized_employee.data)

@api_view(["DELETE"])
def delete_employee(request, pk):
    employee = Employee.objects.get(id = pk)
    employee.delete()
    
    return Response("Employee deleted")


@api_view(["GET"])
def get_departmental_videos(request, department_name):
    department = Department.objects.get(name = department_name)
    departmental_courses = Course.objects.get(department = department)
    departmental_videos = departmental_courses.videos
    seriazlized_videos = VideoSerializer(departmental_videos, many = True)

    return Response(seriazlized_videos.data)

@api_view(["GET"])
def get_video_assessment(request, video_id):
    video = Video.objects.get(id = video_id)
    assessment = Assessment.objects.get(video = video)
    serialized_assessment = AssessmentSerializer(assessment, many = False)

    return Response(serialized_assessment.data)

@api_view(["GET"])
def get_assessment_questions(request, video_id):
    video = Video.objects.get(id = video_id)
    assessment = Assessment.objects.get(video = video)
    assessment_questions = assessment.questions

    serialized_questions = AssessmentQuestionsSerializer(assessment_questions, many  = True)

    return Response(serialized_questions.data)

    

    





