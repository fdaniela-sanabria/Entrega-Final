from django.urls import path
from reviews import views


urlpatterns = [
    
    path("detalle/<pk>/", views.ReviewsDetail.as_view(), name ="reviews_detail"),
    path("crear/", views.ReviewCreate.as_view(), name="review_create"),
    path("editar/<pk>/", views.ReviewUpdate.as_view(), name ="review_update"),
    path("borrar/<pk>/", views.ReviewDelete.as_view(), name ="review_delete"),
    path('lista_reviews/',views.ReviewsList.as_view(), name="reviews_list"),
    path("entrar/", views.ReviewsLogin.as_view(), name="reviews_login"),
    path("salir/", views.ReviewsLogout.as_view(), name="reviews_logout"),
]