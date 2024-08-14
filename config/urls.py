"""
URL configuration for config project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path("", index, name = "index" ),
    path("Recipes/add", add_recipes, name = "add_recipes"),
    path("Recipes/view", view_recipes, name = "view_recipes"),
    path("Recipes/delete<int:id>/", delete_recipes, name = "delete_recipes"),
    path("Recipes/edit<int:id>/", edit_recipes, name = "edit_recipes"),
    path("login", login_page, name = "login_page"),
    path("register", register_page, name = "register_page"),
    path("student", get_students, name = "student"),
    path("see_marks/<student_id>", see_marks, name = "see_marks")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
