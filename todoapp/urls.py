from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('tareas', views.tareas, name='mis_tareas'),
    path('register', views.register_user, name='register_user'), 
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('add_bathroom',views.add_bathroom, name='add_bathroom'),
    #path('list', views.bathroom_list, name='bathroom_list'),
    path('bathroom/<int:id>/', views.bathroom_detail, name='bathroom_detail'),
    path('home', views.home, name='home'),
    path('bathroom2/<int:id>/', views.bathroom_detail2, name='bathroom_detail2'),
]         

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
