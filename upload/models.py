# upload/models.py
from django.db import models

class Upload(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    original_name = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.original_name and self.file:
            self.original_name = getattr(self.file, 'name', '')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.original_name or self.file.name
