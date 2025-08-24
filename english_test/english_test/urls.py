"""
URL configuration for itproger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from content.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tests', TestsPage.as_view()),
    path('testing', TestingPage.as_view()),
	path('result', ResultPage.as_view()),
    path('articles', ArticlesPage.as_view()),
    path('articles_ru', Articles_ruPage.as_view()),
    path('contacts', ContactsPage.as_view()),
    path('how_long_to_learn', How_long_to_learnPage.as_view()),
    path('how_long_to_learn_ru', How_long_to_learn_ruPage.as_view()),
    path('what_is_advanced', What_is_advancedPage.as_view()),
    path('what_is_advanced_ru', What_is_advanced_ruPage.as_view()),
    path('index1_ru', Index1_ruPage.as_view()),
    path('index1', Index1Page.as_view()),
    path('feedback', MessagePage.as_view()),
    path('', HomePage.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

