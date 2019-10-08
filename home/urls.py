from django.urls import path

from . import views
app_name ='home'#uygulamanın adını path ile çağırmak için
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_form),
    path('join', views.join_form),
    path('logout', views.login_out),
    path('panel/<int:id>', views.panel),
    path('contact', views.contact_form, name='contact'),



]