from rest_framework import generics, permissions
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class UploadedFileListCreateView(generics.ListCreateAPIView):
    queryset = UploadedFile.objects.all().order_by("-uploaded_at")
    serializer_class = UploadedFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class UploadedFileDeleteView(generics.DestroyAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    permission_classes = [permissions.IsAuthenticated]

class UploadedFileDownloadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        file_instance = get_object_or_404(UploadedFile, pk=pk)
        return FileResponse(file_instance.file.open(), as_attachment=True, filename=file_instance.filename())
