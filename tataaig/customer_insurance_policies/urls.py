from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'customer_insurance_policies'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('user_list/', views.UserListAPI.as_view(), name='user_list'),
    path('user_policy/<int:usr_id>/', views.UserPolicyList.as_view(), name='user_policy'),
    path('policy_detail/<int:policy_id>/', views.PolicyDetail.as_view(), name='policy_detail'),
    path('user_policy_dump/<int:usr_id>/<str:format_name>/', views.UserPolicyDump.as_view(), name='user_policy_dump')
]
