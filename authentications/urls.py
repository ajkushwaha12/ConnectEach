from django.urls import path
from authentications.views import signup, logout_view, login_view
app_name = "authentications"
urlpatterns = [
    # Other URL patterns...
    path('signup/', signup, name='signup'),
     path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]
