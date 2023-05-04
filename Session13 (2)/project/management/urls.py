from django.urls import path
from management import views

app_name = 'management'
urlpatterns = [
    # management
    path('', views.home, name = 'home'),
]
