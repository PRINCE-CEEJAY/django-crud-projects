from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('profiles/', include('profiles.urls')),
    path('users/', include('users.urls'))
]
