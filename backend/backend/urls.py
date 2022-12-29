from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from runnersclub.views import getcookie, TrainingView, Set_data
route = routers.DefaultRouter()
route.register("trainings", TrainingView, basename="trainings")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/suth/user/me/',getcookie),
    path('data/',Set_data),
    path('api/', include(route.urls)),

]
urlpatterns+=[re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]
