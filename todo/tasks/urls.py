from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index, name= "index"),
    #path("update_tasks/<int:pk>",views.update,name="update_tasks"),
    path("delete/<int:pk>",views.delete,name="delete")
]
