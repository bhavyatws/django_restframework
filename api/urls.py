from django.urls import path
from .  import views
urlpatterns = [
    path('students/', views.students,name='students'),
    path('get-student/', views.getstudent,name='get-student'),
    #Using Class Based View for get-student
    path('get-student-class-based-view/',views.StudentGetView.as_view(),name='get-student-class-based-view'),
    path('students-JsonResponse/', views.students_JsonResponse,name='students'),
    path('student-detail/<int:pk>/', views.student_detail,name='student-detail'),
    path('student-detail-JsonResponse/<int:pk>/', views.student_detail_JsonResponse,name='student-detail'),
    path('student-create/',views.student_create,name="student-create"),
]
