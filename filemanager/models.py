from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return self.file.name.split("/")[-1]

    def size(self):
        return self.file.size

    def mimetype(self):
        import mimetypes
        type_, _ = mimetypes.guess_type(self.file.name)
        return type_ or "application/octet-stream"
