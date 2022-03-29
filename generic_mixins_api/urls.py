from django.urls import path
from .  import views
urlpatterns = [
    #Using generic and mixinx
    path('list-student/', views.StudentList.as_view(),name='student-generic-mixins'),
    path('create-student/', views.CreateStudent.as_view(),name='create-student'),
    path('retreive-student/<int:pk>/', views.RetrieveStudent.as_view(),name='retreive-student'),
    path('update-student/<int:pk>/', views.UpdateStudent.as_view(),name='update-student'),
    path('delete-student/<int:pk>/', views.DeleteStudent.as_view(),name='delete-student'),
    #Combining list and create both together as no pk is required
    path('list-create-student/', views.List_OR_CreateStudentAPI.as_view(),name=';ist-or-create'),
    #Combining retreive,update and delete both together as  pk is required
    path('retreive-update-delete/<int:pk>/',views.Retrieve_Update_Delete_API.as_view(),name='retreive-update-delete'),

]
