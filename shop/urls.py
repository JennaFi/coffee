from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('coffee/', views.coffee_list,
          name='coffee'),
    path('tea/', views.tea_list,
          name='tea'),
    path('index/', views.index, name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

