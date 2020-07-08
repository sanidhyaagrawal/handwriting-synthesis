"""writing_sim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
app_name = 'main' 
urlpatterns = [
    path('', views.home, name='home'),
    path('UserInputText', views.UserInputText, name='UserInputText'),
    path('signup', views.signup, name="signup"),
  	path('create_font', views.create_font, name='create_font'),
  	path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('templateupload', views.templateupload, name='templateupload'),
    path('signupcheck/$', views.signupcheck, name='signupcheck'),
    path('logincheck/$', views.logincheck, name='logincheck'),
    path('preview_tinkering/$', views.preview_tinkering, name='preview_tinkering'),   
    path('save_preview/$', views.save_preview, name='save_preview'),
    path('render_text', views.render_text, name='render_text'),
    path('rendertext', views.rendertext, name='rendertext'),
    path('$your_fonts', views.your_fonts, name='your_fonts'),
    url(r'^(?P<value>\d+)/$', views.deletefont, name='deletefont'),
    url(r'^.*/$', views.view_404)
  ] 
handler400 = 'main.views.view_404' 
handler403 = 'main.views.view_404' 
handler500 = 'main.views.view_404' 
handler404 = 'main.views.view_404' 
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)