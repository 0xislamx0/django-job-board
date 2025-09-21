from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    
)
class Job(models.Model): # table 
    title = models.CharField(max_length=100) # column
    #location
    job_type = models.CharField(max_length=100,choices=JOB_TYPE )
    description = models.TextField(max_length=1000)
    puplished_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vanancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experinace = models.IntegerField(default=1)
    
    def __str__(self): #opject لإرجاع اسم الوظيفة المدخل في قاعدة البيانات وليس كلمة 
        return self.title