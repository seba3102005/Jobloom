from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name = 'index_page'),
    path('offers/',views.job_offers,name='jobOffers'),
    path('login/user/',views.LoginView,name='login'),
    path('register/user/',views.userRegister,name='register_user'),
    path('register/company/',views.companyRegister,name="register_company"),
    path('logout/',views.Logout,name='logout'),
]