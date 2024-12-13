from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home,name='home'),
    path('register/',v.register,name='register'),
    path('login/',v.log_in,name='login'),
    path('logout/',v.log_out,name='logout'),
    path('create/',v.create,name='create'),
    path('update/<str:id>/',v.update,name='update'),
    path('delete/<str:id>/',v.delete_view,name='delete')  

]
 