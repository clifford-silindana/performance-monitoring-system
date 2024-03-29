from rest_framework.serializers import ModelSerializer
from .models import *

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class AssessmentSerializer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"

class AssessmentQuestionsSerializer(ModelSerializer):
    class Meta:
        model = AssessmentQuestion
        fields = "__all__"
