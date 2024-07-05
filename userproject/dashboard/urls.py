from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    path('displayprofile/',views.profile_view,name='displayprofile'),
    path('editprofile/',views.profile_edit,name='editprofile'),
    path('additem/', views.item_add, name='additem'),
    path('edititem/<int:item_id>/',views.item_edit,name='edititem'),

    ]
