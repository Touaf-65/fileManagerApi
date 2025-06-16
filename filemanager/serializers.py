from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    filename = serializers.ReadOnlyField()
    size = serializers.ReadOnlyField()
    mimetype = serializers.ReadOnlyField()
    uploaded_by = serializers.StringRelatedField()

    class Meta:
        model = UploadedFile
        fields = ["id", "filename", "file", "size", "mimetype", "uploaded_at", "uploaded_by"]
        read_only_fields = ["uploaded_at", "uploaded_by"]
