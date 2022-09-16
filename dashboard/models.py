from statistics import mode
from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
   
    
    
    
class vac(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    about = models.TextField()
    due = models.DateTimeField()
    is_finished=models.BooleanField(default=False)
    
    def __str__(self):
        return self.company
    
    
    
    
class s_prof(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    s_name = models.CharField(max_length=50)
    roll_no= models.CharField(max_length=10)
    dob = models.DateField()
    edu = models.CharField(max_length=100)
    email= models.EmailField()
    s_no = models.CharField(max_length=12)
    T_add = models.CharField(max_length=100)
    post_code = models.CharField(max_length=10)
    
    
    
    def __str__(self):
        return self.s_name
    
    
    
    

STATE_CHOICE = (
 ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
 ('Andhra Pradesh','Andhra Pradesh'),
 ('Arunachal Pradesh','Arunachal Pradesh'),
 ('Assam','Assam'),
 ('Bihar','Bihar'),
 ('Chandigarh','Chandigarh'),
 ('Chhattisgarh','Chhattisgarh'),
 ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
 ('Daman and Diu','Daman and Diu'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Haryana','Haryana'),
 ('Himachal Pradesh','Himachal Pradesh'),
 ('Jammu & Kashmir','Jammu & Kashmir'),
 ('Jharkhand','Jharkhand'),
 ('Karnataka','Karnataka'),
 ('Kerala','Kerala'),
 ('Lakshadweep','Lakshadweep'),
 ('Madhya Pradesh','Madhya Pradesh'),
 ('Maharashtra','Maharashtra'),
 ('Manipur','Manipur'),
 ('Meghalaya','Meghalaya'),
 ('Mizoram','Mizoram'),
 ('Nagaland','Nagaland'),
 ('Odisha','Odisha'),
 ('Puducherry','Puducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Sikkim','Sikkim'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telangana'),
 ('Tripura','Tripura'),
 ('Uttarakhand','Uttarakhand'),
 ('Uttar Pradesh','Uttar Pradesh'),
 ('West Bengal','West Bengal'),
)

class Resume(models.Model):
 name = models.CharField(max_length=100)
 dob = models.DateField(auto_now=False, auto_now_add=False)
 gender = models.CharField(max_length=100)
 locality = models.CharField(max_length=100)
 city = models.CharField(max_length=100)
 pin = models.PositiveIntegerField()
 state = models.CharField(choices=STATE_CHOICE, max_length=50)
 mobile = models.PositiveIntegerField()
 email = models.EmailField()
 job_city = models.CharField(max_length=50)
#  profile_image = models.ImageField(upload_to='profileimg', blank=True)
 my_file = models.FileField(upload_to='doc', blank=True)


class Appnow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    jobid =  models.CharField(max_length=100)
    username =  models.CharField(max_length=100)
    name =  models.CharField(max_length=100)
    roll_no =  models.CharField(max_length=100)
    mobile_no =  models.CharField(max_length=100)
    my_file = models.FileField(upload_to='doc', blank=True)
    
    
    def __str__(self):
        return self.jobid
    
        
    
    

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
       verbose_name = "notes"
       verbose_name_plural = "notes"

class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title


class  Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    
         
        
        