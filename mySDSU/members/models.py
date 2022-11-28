from django.db import models

class Students(models.Model):
    redID = models.CharField('Student RedID', max_length = 100)
    email = models.EmailField('Student Email')
    Name = models.CharField('Student Name', max_length = 100)
    Major = models.CharField('Student Major', max_length = 100)
    
    def __str__(self):
        return(self.redID)


class Classes(models.Model):
    courseNumber = models.CharField('Course Number', max_length = 100)
    courseName = models.CharField('Course Name', max_length = 100)
    units = models.CharField('Units', max_length = 100)
    dayAndTime = models.CharField('Day / Time', max_length = 100)
    location = models.CharField('Location', max_length = 100)
    semester = models.CharField('Semester', max_length = 100)
    students_in_class = models.ManyToManyField(Students, blank=True)

    def __str__(self):
        return(self.courseNumber)

class Grades(models.Model):
    courseNumber = models.CharField('Course Number', max_length = 100)
    courseName = models.CharField('Course Name', max_length = 100)
    units = models.CharField('Units', max_length = 100)
    grade = models.CharField('Grade Recieved', max_length = 100)
    gpa = models.CharField('GPA', max_length = 100)
    semester = models.CharField('Semester', max_length = 100)
    students_took_class = models.ManyToManyField(Students, blank=True)

    def __str__(self):
        return(self.courseNumber)