from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('newPassword', views.newAdd, name='newPass'),
    path('del/<int:del_id>', views.deleteEntery, name='del'),
    path('update/<int:id>', views.updateEntery, name='update'),
    
]