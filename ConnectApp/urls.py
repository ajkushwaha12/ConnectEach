
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'ConnectApp'

urlpatterns = [
    path("", views.index, name="index"),
    path("account/login", views.login_view, name="login"),
    path("account/logout", views.logout_view, name="logout"),
    path("account/signup", views.signup_view, name="signup"),
    path("profile/<str:username>", views.profile, name='profile'),
    path("following", views.following, name='following'),
    path("saved", views.saved, name="saved"),
    path("posts/createpost", views.create_post, name="createpost"),
    path("posts/post/<int:id>/like", views.like_post, name="likepost"),
    path("posts/post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("posts/post/<int:id>/save", views.save_post, name="savepost"),
    path("posts/post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("posts/post/<int:post_id>/comments", views.comment, name="comments"),
    path("posts/post/<int:post_id>/write_comment",views.comment, name="writecomment"),
    path("posts/post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("<str:username>/follow", views.follow, name="followuser"),
    path("<str:username>/unfollow", views.unfollow, name="unfollowuser"),
    path("posts/post/<int:post_id>/edit", views.edit_post, name="editpost"),
    path("about", views.about_us, name= "about"),
    path("edit", views.edit_profile, name= "edit"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

