"""mySDSU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from members import views
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('', views.login_user, name = 'Login'),
    path('logout_user', views.logout_user, name = "Logout"),
    path('homepage', views.homePage, name = "homePage"),
    path('myClasses', views.myClasses, name = "myClasses"),
    path('myGrades', views.myGrades, name = 'myGrades'),
    path('applyToGrad', views.applyToGrad, name = 'applyToGrad'),
    path('externalResources', views.externalResources, name = 'externalResources'),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
handler404 = "members.views.page_not_found_view"
