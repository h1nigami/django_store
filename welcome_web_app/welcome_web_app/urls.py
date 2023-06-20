
from django.contrib import admin
from django.urls import path, include
from web_diplom import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('basket/', views.basket, name='basket'),
    path('reviews/', views.rewievs, name='reviews'),
]

