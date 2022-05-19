"""cost_analysis URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cost_analysis import settings
from tender import guest_urls,admin_urls,senior_urls,con_urls
from django.conf.urls.static import static
from tender.views import IndexView, GuestReg, SeniorReg, ContractorReg, LoginView
from django.urls import path
urlpatterns = [
    path('', IndexView.as_view()),
    path('gust_reg', GuestReg.as_view()),
    path('senior_reg',SeniorReg.as_view()),
    path('contractor_reg',ContractorReg.as_view()),
    path('admin/',admin_urls.urls()),
    path('gust/',guest_urls.urls()),
    path('senior/',senior_urls.urls()),
    path('contractor/',con_urls.urls()),
    path('login', LoginView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)