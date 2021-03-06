"""spider_web URL Configuration

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
from django.conf.urls import url
from spider_page import views
from . import longyi_tjzq_db

urlpatterns = [
    url(r'^accounts/login/', views.login),
    url(r'^admin/', admin.site.urls),
    url('^index/', views.index),
    # url(r'^longyi_tjzq$', longyi_tjzq_db.slec_all),
    url(r'^longyi_tjzq/', views.longyi_tjzq, name="reg1_1_1"),
    url(r'^longyi_yp/', views.longyi_yp, name="reg1_1_2"),
    url(r'^rjyiyao_xpsj/', views.rjyiyao_xpsj, name="reg2_1_1"),
    url(r'^rjyiyao_zkzq/', views.rjyiyao_zkzq, name="reg2_1_2"),
    url(r'^scjrm_zszq/', views.scjrm_zszq, name="reg3_1_1"),
    url(r'^scjuchuang_py/', views.scjuchuang_py, name="reg4_1_1"),
    url(r'^scjuchuang_tjzq/', views.scjuchuang_tjzq, name="reg4_1_2"),
    url(r'^scjuchuang_yxzq/', views.scjuchuang_yxzq, name="reg4_1_3"),
    url(r'^scjuchuang_jtj/', views.scjuchuang_jtj, name="reg4_1_4"),
    url(r'^sckxyy_ypzq/', views.sckxyy_ypzq, name="reg5_1_1"),
    url(r'^scytyy_zszq/', views.scytyy_zszq, name="reg6_1_1"),
    url(r'^scytyy_tjzq/', views.scytyy_tjzq, name="reg6_1_2"),
    url(r'^ysbang_zxxd/', views.ysbang_zxxd, name="reg7_1_1"),
    url(r'^hezongyy_py/', views.hezongyy_py, name="reg8_1_1"),
    url(r"longyi1", views.start_longyi_tjzq, name="reg1_1"),
    url(r"longyi2", views.start_longyi_yp, name="reg1_2"),
    url(r"rjyiyao1", views.start_rjyiyao_xpsj, name="reg2_1"),
    url(r"rjyiyao2", views.start_rjyiyao_zkzq, name="reg2_2"),
    url(r"scjrm", views.start_scjrm_zszq, name="reg3_1"),
    url(r"scjuchuang1", views.start_scjuchuang_py, name="reg4_1"),
    url(r"scjuchuang2", views.start_scjuchuang_tjzq, name="reg4_2"),
    url(r"scjuchuang3", views.start_scjuchuang_yxzq, name="reg4_3"),
    url(r"scjuchuang4", views.start_scjuchuang_jtj, name="reg4_4"),
    url(r"sckxyy", views.start_sckxyy_ypzq, name="reg5_1"),
    url(r"scytyy1", views.start_scytyy_tjzq, name="reg6_1"),
    url(r"scytyy2", views.start_scytyy_zszq, name="reg6_2"),
    url(r"ysbang", views.start_ysbang_zxxd, name="reg7_1"),
    url(r"hezongyy", views.start_hezongyy_py, name="reg8_1"),
    # url('^', views.start_rjyiyao_xpsj),
    # url('^', views.start_longyi_tjzq),
    path("test_demo/", views.test_demo),
    path("test_demo2/", views.test_demo2),

]
