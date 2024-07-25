from django.urls import path
from .views import List,Detail,Create,Delete,Update,EndList,signupfunc,loginfunc,Logout

urlpatterns = [
    path('list/',List.as_view(),name='list'),
    path('detail/<int:pk>',Detail.as_view(),name='detail'),
    path('create/',Create.as_view(),name='create'),
    path('delete/<int:pk>',Delete.as_view(),name='delete'),
    path('update/<int:pk>',Update.as_view(),name='update'),
    path('end_list/',EndList.as_view(),name='end_list'),
    path('signup/',signupfunc,name='signup'),
    path('login/',loginfunc,name='login'),
    path('logout/',Logout.as_view(),name='logout')
]
