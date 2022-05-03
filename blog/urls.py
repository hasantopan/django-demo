from django.urls import path
from blog.views import iletisim, anasayfa
from blog.views.anasayfa import anasayfa
    

urlpatterns = [
    path('',anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name ='iletisim'),
]