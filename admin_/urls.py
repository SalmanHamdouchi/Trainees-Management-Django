"""
Stage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', views.view_profile, name='profile'),
    path('changep/', views.change_password, name='change_password'),
    path('ajout/', views.ajout_stagiaire, name='ajout'),
    path('stagiaire/<str:cne>', views.view_stagiaire, name='info'),
    path('supp/<str:cne>', views.supp_stagiaire, name='supp'),
    path('update/<str:cne>', views.update_stagiaire.as_view(template_name='admin_/update.html'), name='update'),
    path('absence/', views.marquer_absence, name='absence'),
    path('login/', auth_views.LoginView.as_view(template_name='admin_/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='admin_/login.html'), name='logout'),
    path('afficher_tout', views.afficher_tout, name='stagiaire_list'),
    path('cv/<str:cne>', views.pdf_view, name='pdf_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
