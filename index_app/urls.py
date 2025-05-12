from django.urls import path
from index_app.views import PhotoView, PhotoListView, CreatePhotoView

app_name = "index_app"

urlpatterns = [
    path("", PhotoListView.as_view(), name="photo-list"),
    path("photo/", PhotoView.as_view(), name="photo"),
    path("create-photo/", CreatePhotoView.as_view(), name="create-photo"),
]
