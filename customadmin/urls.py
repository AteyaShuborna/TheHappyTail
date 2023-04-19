from django.urls import path
from .views import admin_login,admin_dashboard,view_all_adoption_request,approve_adoption_request,logout_admin

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('all-adoption-request/', view_all_adoption_request, name='all_adoption_request'),
    path('<int:pk>/approve-adoption-request', approve_adoption_request, name='approve_adoption_request'),
    path('admin-logout', logout_admin, name='admin_logout'),
]