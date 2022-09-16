from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from dashboard import views as dash_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.g_index,name="home"),
    path('stu_erp',views.stu_erp,name="stu_erp"),
    path('g_index',views.g_index,name="g_index"),
    path('g_profile',views.g_profile,name="g_profile"),
    
    path('profile1', views.profileView.as_view(), name='profile1'),
    
    path('<int:pk>', views.CandidateView.as_view(), name='candidate'),
  
    
  
    
    
    path('post_vac',views.post_vac,name="post_vac"),
    path('update_vacancy/<int:pk>',views.update_vacancy,name="update-vacancy"),
    path('delete_vacancy/<int:pk>',views.delete_vacancy,name="delete-vacancy"),
    
    
    path('apply_vacancy',views.apply_vacancy,name="apply_vacancy"),
    
    
    path('stu_profile',views.stu_profile,name="stu_profile"),
    
    path('profile2',views.profile2,name="profile2"),
    
    path('viewdata',views.viewdata,name="viewdata"),
    
    path('viewdata2',views.viewdata2,name="viewdata2"),
    
    
    
    
    path('notes',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name="delete-note"),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"), 
    
    path('homework',views.homework,name="homework"),
    path('update_homework/<int:pk>',views.update_homework,name="update-homework"),
    path('delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),

    path('youtube',views.youtube,name="youtube"),

    path('todo',views.todo,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name="update-todo"),
    path('delete_todo/<int:pk>',views.delete_todo,name="delete-todo"),


    path('books',views.books,name="books"),

    path('dictionary',views.dictionary,name="dictionary"),

    path('wiki',views.wiki,name="wiki"),

    path('conversion',views.conversion,name="conversion"),
    
    # path('register',views.register,name="register"),
    # path('login',views.login,name="login"),
    # # path('logout',views.logout,name="logout"),
    
    
    path('register/',dash_views.register,name ='register'),
    path('login/',auth_views.LoginView.as_view(template_name="dashboard/login.html"),name ='login'),
    path('profile/',dash_views.profile,name='profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name="dashboard/logout.html"),name ='logout'),

   
   
   
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)