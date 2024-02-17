"""
URL configuration for testweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from testapp import views

#urlpatterns = [
patterns = [
    #path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('', views.index, name='index'),
    path('', include('testapp.urls')),
    re_path(r'^about/.*', views.about, name='about'),
    #re_path(r'^user/(?P<name>.+)', views.user, name='user'),
    #re_path(r'^user', views.user, name='user-default'),
    path('user/', views.user, name='user'),
    path('register/', views.register, name='register'),
    path("edit/<str:name>/", views.edit),
    path("delete/<str:name>/", views.delete),
    path('admin/', admin.site.urls),
    #path('<str:user_exist><str:user_not_exist><str:welcome>', views.index, name='index'),
]

#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
from rest_framework import permissions

schema_view = get_schema_view(  # new
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    # url=f'{settings.APP_URL}/api/v3/',
    patterns=patterns,
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    #path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('', views.index, name='index'),
    #path('', include('testapp.urls')),
    re_path(r'^about/.*', views.about, name='about'),
    #re_path(r'^user/(?P<name>.+)', views.user, name='user'),
    #re_path(r'^user', views.user, name='user-default'),
    path('user/', views.user, name='user'),
    path('register/', views.register, name='register'),
    path("edit/<str:name>/", views.edit),
    path("delete/<str:name>/", views.delete),
    path('admin/', admin.site.urls),
    #path('<str:user_exist><str:user_not_exist><str:welcome>', views.index, name='index'),
    path(  # new
        'swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    re_path(  # new
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    path('', include('testapp.urls')),
    #path('sns/', include('ses_sns.urls')),
    path('admin/', admin.site.urls),
    #path('ckeditor/', include('ckeditor_uploader.urls')),
]
