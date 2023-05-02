from django.urls import path
from .views import admin_login,admin_dashboard,view_all_adoption_request,approve_adoption_request,logout_admin,view_all_users,admin_view_userprofile,delete_userprofile
from post.views import view_all_adoption_post,view_all_missing_post
urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('all-adoption-request/', view_all_adoption_request, name='all_adoption_request'),
    path('all-users/', view_all_users, name='all_users'),
    path('<int:pk>/approve-adoption-request', approve_adoption_request, name='approve_adoption_request'),
    path('<int:pk>/view-userprofile',admin_view_userprofile, name='admin_view_user_profile'),
    path('<int:pk>/delete-userprofile',delete_userprofile, name='delete_user_profile'),
    path('admin-logout', logout_admin, name='admin_logout'),
    path('all-adoption-post/', view_all_adoption_post, name='all_adoption_post'),
    path('all-missing-post/', view_all_missing_post, name='all_missing_post'),
]