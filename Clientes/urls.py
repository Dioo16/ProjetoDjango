
from django.contrib import admin
from django.urls import path
from .views import person_list, person_update,person_new,person_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', person_list,name="person_list"),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>', person_update, name="person_update"),
    path('list/<int:id>',person_delete, name="person_delete")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
