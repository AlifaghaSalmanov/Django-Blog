from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "article"

urlpatterns = [
    path("", views.articles, name="articles"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("addarticle/", views.addarticle, name="addarticle"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("comment/<int:id>", views.addComment, name="comment"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
