from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from runnersclub.views import getcookie

urlpatterns = [
        path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/suth/user/me/',getcookie),

]

urlpatterns+=[re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]