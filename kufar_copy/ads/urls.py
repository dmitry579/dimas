from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('<int:pk>/', views.ad_detail, name='ad_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)