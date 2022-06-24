from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from usuarios import views

urlpatterns = [
    path("crear/", views.UserSignUp.as_view(), name ="user_signup"),
    path("profile/<pk>/", views.UserProfile.as_view(), name ="user_profile"),
    path("editar/<pk>/", views.UserUpdate.as_view(), name ="user_edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)