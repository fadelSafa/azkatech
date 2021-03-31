from django.conf.urls import url
from my_app import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
     url(r'^$',views.index,name='index'),
     url(r'^about/',views.about,name='about'),
     path('dashboard/vacations/add_vacation/',views.add_vacation,name="add_vacation"),
     path('dashboard/vacations/delete_vacation/',views.delete_vacation,name="delete_vacation"),
     path('dashboard/vacations/update_vacation',views.update_vacation,name="update_vacation"),
     path('dashboard/',views.dashboardView,name="dashboard"),
     path('dashboard/vacations',views.vacation,name="vacations"),
     path('dashboard/vacations/get-data',views.get_vacation,name="get_vacations"),
     path('login/',LoginView.as_view(),name="login_url"),
     path('register/',views.registerView,name="register_url"),

]

