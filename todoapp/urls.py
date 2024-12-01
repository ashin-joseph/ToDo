from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.home, name="home"),
    path('save',views.save, name="save"),
    path('display_task',views.display_task, name="display_task"),
    path('update_task/<int:uid>/',views.update_task, name="update_task"),
    path('update_save_task/<int:uid>/',views.update_save_task, name="update_save_task"),
    path('delete_todo/<int:did>/',views.delete_todo, name="delete_todo")

]