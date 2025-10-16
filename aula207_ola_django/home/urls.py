from django.urls import path
from home import views

# Http Request <-> Http Response
# MVT (MVC)

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),

]