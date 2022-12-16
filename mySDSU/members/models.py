from django.db import models
from django.contrib.auth.models import User

class Classes(models.Model):
    courseNumber = models.CharField('Course Number', max_length = 100)
    courseName = models.CharField('Course Name', max_length = 100)
    units = models.CharField('Units', max_length = 100)
    dayAndTime = models.CharField('Day / Time', max_length = 100)
    location = models.CharField('Location', max_length = 100)
    semester = models.CharField('Semester', max_length = 100)
    students = models.ManyToManyField(User)

    def __str__(self):
        return(self.courseNumber)

class Grades(models.Model):
    courseNumber = models.CharField('Course Number', max_length = 100)
    courseName = models.CharField('Course Name', max_length = 100)
    units = models.CharField('Units', max_length = 100)
    grade = models.CharField('Grade Recieved', max_length = 100)
    gpa = models.CharField('GPA', max_length = 100)
    semester = models.CharField('Semester', max_length = 100)
    students = models.ManyToManyField(User)

    def __str__(self):
        return(self.courseNumber)

class appointment(models.Model):
    redID = models.CharField('RedID', max_length = 9)
    advisor = models.CharField('Advisor', max_length = 100)

    def __str__(self):
        return(self.redId)

class applyToGrad(models.Model):
    firstName = models.CharField('First Name', max_length = 30)
    lastName = models.CharField('Last Name', max_length = 50)
    redID = models.CharField('RedID', max_length = 9)
    catalogYear = models.CharField('Catalog Year', max_length = 4)
    major = models.CharField('Major', max_length = 100)

    def __str__(self):
        return(self.redId)