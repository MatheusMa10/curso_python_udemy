from django.urls import path
from blog import views

# Http Request <-> Http Response
# MVT (MVC)

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo')
]