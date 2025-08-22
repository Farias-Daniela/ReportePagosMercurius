# uploads/views.py
from django.shortcuts import render
from .forms import UploadForm
from .models import Upload

def upload_view(request):
    uploaded = None

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.save()
            # Resetea el form después de guardar
            form = UploadForm()
    else:
        form = UploadForm()

    # muestra últimos 5 archivos
    last_uploads = Upload.objects.order_by('-uploaded_at')[:5]

    return render(request, 'upload/upload.html', {
        'form': form,
        'uploaded': uploaded,
        'uploads': last_uploads
    })

