


from django.contrib import admin
from django.urls import path, re_path
from app.views import *
from django.contrib.auth.views import LoginView, LogoutView
# from app.views import viewer

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', loggining, name='loggining'),
    path('yeslog/', LoginView.as_view(template_name='yeslog.html'), name='yeslog'),
    path('nelog/', nelog, name='nelog'),
] 




