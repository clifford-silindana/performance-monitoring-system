from django.db import models

class Department(models.Model):
    name = models.CharField(max_length = 50)
    physical_address = models.TextField()

class Designation(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    required_skills = models.TextField()
    education_requirements = models.TextField()
    department = models.ForeignKey(Department, on_delete = models.DO_NOTHING)

class Employee(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    date_of_birth = models.DateField()
    physical_address = models.CharField(max_length = 100)
    designation = models.ForeignKey(Designation, on_delete = models.DO_NOTHING)
    date_of_hire = models.DateField(null = True, blank = True)
    email_address = models.EmailField(max_length = 50)
    cell_number = models.CharField(max_length = 30)
    salary = models.IntegerField(null = True)

    def __str__(self):
        return self.first_name + self.designation.title

class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)


class EmployeeProject(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.DO_NOTHING)

class ProjectTask(models.Model):
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length = 20)

class EmployeeProjectTask(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    task_no = models.ForeignKey(ProjectTask, on_delete = models.DO_NOTHING)

class Role(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    required_skills = models.TextField()
    education_requirements = models.TextField()


class Payment(models.Model):
    employee_paid = models.ForeignKey(Employee, on_delete = models.CASCADE, null = True, blank = True)
    amount_paid = models.CharField(max_length = 10)
    payment_date = models.DateTimeField(auto_now_add = True)
    payment_method = models.TextField()

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    attendance = models.DateTimeField(auto_now = True)
    time_in = models.TimeField(auto_now_add = True)
    time_out = models.TimeField(auto_now_add = True)
    total_hours_worked = models.IntegerField()

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    type_of_leave = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()

class Overtime(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    request_reason = models.TextField()
    request_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 20)
    outcome_date = models.DateField(auto_now_add = True)

class Video(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    url = models.CharField(max_length = 300)
    date_uploaded = models.DateTimeField(auto_now_add = True)

class Course(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    students = models.ManyToManyField(Employee, null = True, blank = True)
    department = models.ForeignKey(Department, on_delete = models.DO_NOTHING, null = True, blank = True)
    category = models.CharField(max_length = 100)
    videos = models.ManyToManyField(Video, null = True, blank = True)  

class AssessmentQuestion(models.Model):
    question = models.TextField()
    answer_type = models.CharField(max_length = 100)

class Assessment(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date_created = models.DateField(auto_now = True)
    start_date = models.DateField(null = True, blank = True)
    due_date = models.DateField(null = True, blank = True)
    course = models.ManyToManyField(Course)
    video = models.ManyToManyField(Video, null=True, blank=True)
    questions = models.ManyToManyField(AssessmentQuestion, null = True, blank = True)

class Mark(models.Model):
    student = models.ForeignKey(Employee, on_delete = models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete = models.CASCADE)
    grade = models.CharField(max_length = 10)
    comments = models.TextField(null = True, blank = True)














