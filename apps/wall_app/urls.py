from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall_display),
    path('logout', views.logout),
    path('post', views.post_message),
    path('comment', views.post_comment),
    path('delete/<int:message_id>', views.delete_message)
]