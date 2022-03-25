from django.urls import path
from .  import views
urlpatterns = [
   
    path('get-student/', views.getstudent,name='get-student'),
    #Using Class Based View for get-student
    path('get-student-class-based-view/',views.StudentGetView.as_view(),name='get-student-class-based-view'),
    #api_view
    path('hello-world/',views.hello_world,name='hello-world'),
    path('student-api-view/',views.student_api_view,name='student-api-view'),
    #pk is passing here in function
    path('student-api-view-pk/',views.student_api_view_pk,name='student-api-view-pk'),
    path('student-api-view-pk/<int:pk>/',views.student_api_view_pk,name='student-api-view-pk'),
    #Class Based APIView
    path('student-classbased-apiview/',views.StudentClassBasedAPI.as_view(),name='class-based-apiview')
  
]
