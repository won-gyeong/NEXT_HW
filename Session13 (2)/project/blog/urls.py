from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('update/<int:post_id>', views.update, name='update'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('delete_comment/<int:post_id>/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('recomment/<int:post_id>/<int:comment_id>', views.recomment, name='recomment'),
    path('delete_recomment/<int:post_id>/<int:comment_id>/<int:recomment_id>/', views.delete_recomment, name='delete_recomment'),
    path("registration/signup/", views.signup, name="signup"),
    path("registration/login/", views.login, name="login"),
    path("registration/logout/", views.logout, name="logout"), 
]