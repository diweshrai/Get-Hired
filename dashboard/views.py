from cgitb import text
from multiprocessing import context
from tkinter.tix import Form
from django.shortcuts import redirect, render
from dashboard.models import s_prof
from django.views import View

from dashboard.models import Resume


import dashboard
from . forms import *
from django.contrib import messages
from django.views import generic
from django.forms.widgets import FileInput
from youtubesearchpython import VideosSearch
import requests
import wikipedia 
from django.contrib.auth.decorators import login_required   

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def stu_erp(request):
    return render(request,'dashboard/stu_erp.html')


def g_profile(request):
    return render(request,'dashboard/g_profile.html')


def stu_profile(request):
    return render(request,'dashboard/stu_profile.html')


def profile2(request):
    return render(request,'dashboard/profile2.html')


def viewdata(request):
    if request.method == "POST":
        form = appnow(request.POST)
        if form.is_valid():
            viewdatas=Appnow(
                user=request.user,
                jobid=request.POST['jobid'],
                username=request.POST['username'],
                name=request.POST['name'],
                roll_no=request.POST['roll_no'],
                mobile_no=request.POST['mobile_no'],
                my_file=request.POST['my_file'],
            )
            viewdatas.save()
            messages.success(request,f'SUCCESSFULLY APPLIED{request.user.username}!!')
    else:
        form = Post()
    
    
    form = appnow()
    
    
    context ={
        'form':form,
        'viewdatas':viewdata
    }
    
    
    return render(request,'dashboard/viewdata.html' , context)


def viewdata2(request):
    viewdata2 = Appnow.objects.filter(user=request.user)
    context = {'viewdata2s':viewdata2}
    
    return render(request,'dashboard/viewdata2.html' , context)


@login_required
def g_index(request):
    vacancys = vac.objects.filter(is_finished =False,user=request.user)
    if len(vacancys) == 0:
        vacancy_done = True
    else:
        vacancy_done = False 
        
        
    context = {
        'vacancys' : vacancys,
        'vacancy_done': vacancy_done,
        
    }    
    
    
    
    
    return render(request,'dashboard/g_index.html',context)







def post_vac(request):
    if request.method == "POST":
        form = Post(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            vacancy =vac(
                user = request.user,
                company = request.POST['company'],
                designation = request.POST['designation'],
                about = request.POST['about'],
                due = request.POST['due'],
                is_finished = finished

            )     
            vacancy.save()
            messages.success(request,f'Vacancy Added from {request.user.username}!!')
    else:
        form = Post()
    vacancy = vac.objects.filter(user=request.user)
    if len(vacancy) == 0:
        homework_done = True
    else:
        homework_done = False    
    context = {
        'vacancys':vacancy,
        'vacancy_done':homework_done,
        'form':form,
        }
   
    
    return render(request,'dashboard/post_vac.html', context)



def update_vacancy(request,pk=None):
    vacancy = vac.objects.get(id=pk)
    if vacancy.is_finished == True:
        vacancy.is_finished = False
    else:
        vacancy.is_finished = True
    vacancy.save()
    return redirect('post_vac')            


def delete_vacancy(request,pk=None):
    vac.objects.get(id=pk).delete()
    return redirect('post_vac')





def apply_vacancy(request):
    vacancys = vac.objects.filter(is_finished =False,user=request.user)
    if len(vacancys) == 0:
        vacancy_done = True
    else:
        vacancy_done = False 
        
        
    context = {
        'vacancys' : vacancys,
        'vacancy_done': vacancy_done,
        
    }    
    return render(request,'dashboard/apply_vacancy.html',context)



class profileView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()
  return render(request, 'dashboard/profile1.html', { 'candidates':candidates,'form':form})



 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'dashboard/profile1.html', {'form':form})


class CandidateView(View):
 def get(self, request,pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'dashboard/candidate.html' , {'candidate':candidate})

# def s_profile(request):
#     if request.method == "POST":
#         s_name= request.POST.get('s_name')
#         roll_no= request.POST.get('roll_no')
#         dob= request.POST.get('dob')
#         edu= request.POST.get('edu')
#         email= request.POST.get('email')
#         s_no= request.POST.get('s_no')
#         T_add= request.POST.get('T_add')
#         post_code= request.POST.get('post_code')
#         s_profile = s_prof(s_name=s_name, roll_no= roll_no, dob=dob
#                           edu=edu, email=email,s_no=s_no,T_add=T_add
#                           post_code=post_code)
        
#         s_profile.save()
#     return render(request, 'profile2.html')    






# def s_profile(request):
#     if request.method == "POST":
#         form = student_profile(request.POST)
#         if form.is_valid():
#             s_profiles =s_prof(
#                 user = request.user,
#                 s_name = request.POST['s_name'],
#                 roll_no = request.POST['roll_no'],
#                 dob = request.POST['dob'],
#                 edu = request.POST['edu'],
#                 email = request.POST['email'],
#                 s_no = request.POST['s_no'],
                
#                 T_add = request.POST['T_add'],
#                 post_code = request.POST['post_code']

#             )     
#             s_profiles.save()
#             messages.success(request,f'Homework Added from {request.user.username}!!')
#     else:
#         form = student_profile()
#     homework = student_profile.objects.filter(user=request.user)
#     context = {
#         's_profiles':s_profile,
#         'form':form,
#         }
#     return render(request,'dashboard/g_profile.html',context)







@login_required
def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added from {request.user.username}Succcesfully!")
    else:        
      form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context) 

@login_required
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")  


class NotesDetailView(generic.DetailView):
    model =Notes

@login_required
def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homeworks =Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished

            )     
            homeworks.save()
            messages.success(request,f'Homework Added from {request.user.username}!!')
    else:
        form = HomeworkForm()
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False    
    context = {
        'homeworks':homework,
        'homeworks_done':homework_done,
        'form':form,
        }
    return render(request,'dashboard/homework.html',context)

@login_required
def update_homework(request,pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')            

@login_required
def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')

def youtube(request):
    if request.method == "POST":
        form = DashboardFom(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i ['descriptionSnippet']:
                    desc +=j['text']
            result_dict['description'] = desc
            result_list.append(result_dict) 
            context={
                'form':form,
                'results' : result_list
            }  
        return render(request,'dashboard/youtube.html',context)         
    else:
        form = DashboardFom()
    context = {'form':form}
    return render(request,'dashboard/youtube.html',context)

@login_required
def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished =  request.POST["is_finished"]
                if finished =='on':
                    finished = True
                else :
                    finished = False
            except:
                finished = False
            todos = Todo(
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            )                
            todos.save()
            messages.success(request,f"Todo Added from {request.user.username}!!")
    else:        
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False    
    context = {
        'form': form,
        'todos':todo,
        'todos_done':todos_done
    }
    return render(request,'dashboard/todo.html',context)    

@login_required
def update_todo(request,pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')  

@login_required
def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()  
    return redirect('todo') 


def books(request):
    if request.method == "POST":
        form = DashboardFom(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer =r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pagerating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink')

            }
            result_list.append(result_dict) 
            context={
                'form':form,
                'results' : result_list
            }  
        return render(request,'dashboard/books.html',context)         
    else:
        form = DashboardFom()
    context = {'form':form}
    return render(request,'dashboard/books.html',context) 

def dictionary(request):
    if request.method == "POST":
        form = DashboardFom(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer =r.json()
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context = {
                'form': form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms
            }
        except:
            context = {
                'form':form,
                'input':''
            }  
        return render(request,"dashboard/dictionary.html",context) 
    else:        
        form = DashboardFom()
        context = {'form':form
        }
    return render(request,"dashboard/dictionary.html",context)  

def wiki(request):
    if request.method == 'POST':
        text = request.POST['text']
        form = DashboardFom(request.POST)
        search = wikipedia.page(text)
        context = {
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary
        }
        return render(request,"dashboard/wiki.html",context)
    else:    
        form = DashboardFom()
        context = {
        'form':form
        }
    return render(request,"dashboard/wiki.html",context)  

def conversion(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if request.POST['measurement'] == 'length':
            measurement_form = ConversionLengthForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            } 
            if  'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first =='yard' and second =='foot':
                        answer = f'{input} yard = {int(input)*3} foot'
                    if first =='foot' and second =='yard':
                        answer = f'{input} foot = {int(input)/3} yard'
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                } 
        if request.POST['measurement'] == 'mass':
            measurement_form = ConversionMassForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            } 
            if  'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first =='pound' and second =='kilogram':
                        answer = f'{input} pound = {int(input)*0.43592} kilogram'
                    if first =='kilogram' and second =='pound':
                        answer = f'{input} kilogram = {int(input)*2.20462} pound'
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }                               
    else:
        form = ConversionForm()
        context = {
         'form':form,
         'input':False
        }  
    return render(request,"dashboard/conversion.html",context)  

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}!!")
            return redirect("login")
    else:        
        form = UserRegistrationForm()
    context = {
        'form':form
    }
    return render(request,"dashboard/register.html",context)

@login_required
def profile(request):
    homeworks = Homework.objects.filter(is_finished =False,user=request.user)
    todos = Todo.objects.filter(is_finished= False,user=request.user)
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False  
    if len(todos) == 0:
        todos_done = True      
    else:
        todos_done = False
    context = {
        'homeworks' : homeworks,
        'todos': todos,
        'homework_done': homework_done,
        'todos_done': todos_done
    }        
    return render(request,"dashboard/profile.html",context)    
