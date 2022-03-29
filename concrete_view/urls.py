from django.urls import path
from .  import views
urlpatterns = [
    #Using Concrete View
    path('list-student/', views.StudentList.as_view(),name='ist-student'),
    path('create-student/', views.StudentCreate.as_view(),name='create-student'),
    path('retreive-student/<int:pk>/', views.StudentRetreive.as_view(),name='retreive-student'),
    path('update-student/<int:pk>/', views.StudentUpdate.as_view(),name='update-student'),
    path('delete-student/<int:pk>/', views.StudentDelete.as_view(),name='delete-student'),
    path('list-create-student/', views.StudentListCreate.as_view(),name='list-create-student'),
    path('retreive-update-delete/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view(),name='retreive-update-delete'),
    # #Combining list and create both together as no pk is required
    # path('list-create-student/', views.List_OR_CreateStudentAPI.as_view(),name=';ist-or-create'),
    # #Combining retreive,update and delete both together as  pk is required
    # path('retreive-update-delete/<int:pk>/',views.Retrieve_Update_Delete_API.as_view(),name='retreive-update-delete'),

]
