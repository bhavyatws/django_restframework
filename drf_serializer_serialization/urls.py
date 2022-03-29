"""drf_serializer_serialization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path,include
from viewset import views
# from modelviewset import views
from authentication import views
#viewset default router
from rest_framework.routers import DefaultRouter
#Creating Router Object
router=DefaultRouter()
#Register StudentViewSet with Router
# router.register('student-api',views.StudentViewSet,basename='student-api')
router.register('student-api',views.StudentModelViewSet,basename='student-api')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('modelserializor/', include('modelserializor.urls')),
    path('generic-mixins-api/', include('generic_mixins_api.urls')),
    path('concrete-view-api/', include('concrete_view.urls')),
    path('viewsetapi/', include(router.urls)),
    path('authentication-modelviewset/', include(router.urls)),
]
