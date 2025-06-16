from django.urls import path
from .views import UploadedFileListCreateView, UploadedFileDeleteView, UploadedFileDownloadView

urlpatterns = [
    path("", UploadedFileListCreateView.as_view(), name="file-list-create"),
    path("<int:pk>/delete/", UploadedFileDeleteView.as_view(), name="file-delete"),
    path("<int:pk>/download/", UploadedFileDownloadView.as_view(), name="file-download"),
]
