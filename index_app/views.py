from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from index_app.forms import PhotoForm
from index_app.handlers import handle_uploaded_file, save_image
from index_app.fetchers import (
    fetch_uploaded_files,
    fetch_binary_image,
    fetch_ip_camera_path,
)


class CreatePhotoView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        camera_ip = request.GET.get("camera_ip", "192.168.1.10")
        binary_image = fetch_binary_image(fetch_ip_camera_path(camera_ip))
        if binary_image is not None:
            image_name = request.GET.get("image_name", "image")
            save_image(f"{image_name}.jpg", binary_image)
        return redirect("index_app:photo-list")


class PhotoView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request=request,
            template_name="index_app/photo.html",
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo_name = photo_form.cleaned_data.get("photo_name")
            file = photo_form.cleaned_data.get("photo")
            handle_uploaded_file(f"{photo_name}.jpg", file)
            return redirect("index_app:photo-list")
        return redirect("index_app:photo")


class PhotoListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        photos = fetch_uploaded_files()
        return render(
            request=request,
            template_name="index_app/index.html",
            context={"photos": photos},
        )
