from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('signup/', views.signuppage, name='signuppage'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('detail/', views.detail_view, name='detail_view'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('result/<str:aluminum>/<str:location>/', views.result, name='result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
